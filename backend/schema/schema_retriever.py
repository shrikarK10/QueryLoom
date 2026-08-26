import re
from collections import defaultdict


EXACT_MATCH_WEIGHT = 1.0
TOKEN_MATCH_WEIGHT = 0.6
MORPHOLOGY_MATCH_WEIGHT = 0.3
COLUMN_EVIDENCE_WEIGHT = 0.4


def _normalize_token(text: str) -> str:
    """Normalize text by converting to lowercase and stripping punctuation."""
    return text.lower().strip()


def _singularize(word: str) -> str:
    """Simple deterministic singularization for common schema terms."""
    w = word.lower()
    if w.endswith("ies") and len(w) > 4:
        return w[:-3] + "y"
    if w.endswith("es") and len(w) > 3 and w[-3] not in "aeiou":
        return w[:-2]
    if w.endswith("s") and not w.endswith("ss") and len(w) > 3:
        return w[:-1]
    return w


def _split_identifier(name: str) -> list[str]:
    """
    Splits CamelCase, PascalCase, or snake_case identifiers into constituent words.
    Example: 'SalesOrderHeader' -> ['sales', 'order', 'header']
             'Customer_ID' -> ['customer', 'id']
    """
    # Replace underscores with spaces
    s = name.replace("_", " ")
    # Insert space before capital letters following lowercase letters
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", s)
    tokens = re.findall(r"\b\w+\b", s)
    return [t.lower() for t in tokens if t]


class SchemaRetriever:
    """
    Lexical schema retriever that ranks database tables and columns by query relevance.

    Signals evaluated per token-pair (using strongest signal only):
    1. Exact Match (1.0)
    2. Token Match (0.6)
    3. Morphology Match (0.3)

    Evidence propagation:
    - Column matches propagate COLUMN_EVIDENCE_WEIGHT (0.4) boost to parent table.

    No score cutoff is enforced in retrieve(); complete ranked list is returned.
    """

    def __init__(self, catalog):
        self.catalog = catalog

    def _extract_query_tokens(self, query: str) -> list[dict]:
        """
        Extracts raw tokens and their singularized versions from natural language query.
        """
        raw_words = re.findall(r"\b\w+\b", query.lower())
        tokens = []
        for word in raw_words:
            tokens.append({
                "raw": word,
                "singular": _singularize(word)
            })
        return tokens

    def _evaluate_lexical_signal(self, query_token: dict, identifier: str) -> tuple[float, str | None]:
        """
        Evaluates the strongest lexical signal between a query token and a schema identifier.
        Returns (score, reason_type).
        """
        q_raw = query_token["raw"]
        q_sing = query_token["singular"]
        id_norm = identifier.lower()

        # 1. Exact Match
        if q_raw == id_norm:
            return EXACT_MATCH_WEIGHT, "exact"

        # 2. Token Match (for multi-word/CamelCase identifiers)
        id_split_tokens = _split_identifier(identifier)
        if len(id_split_tokens) > 1 and q_raw in id_split_tokens:
            return TOKEN_MATCH_WEIGHT, "token"

        # 3. Morphology Match
        if q_sing == id_norm or (len(id_split_tokens) > 0 and any(q_sing == _singularize(t) for t in id_split_tokens)):
            return MORPHOLOGY_MATCH_WEIGHT, "morphology"

        return 0.0, None

    def retrieve(self, query: str) -> dict:
        """
        Ranks tables and columns in the catalog for the given query.

        Returns:
        {
            "tables": [
                {
                    "table": "Product",
                    "score": 1.4,
                    "matched_terms": ["product", "price"],
                    "reasons": ["exact_table_match:product", "column_evidence:ListPrice"]
                }, ...
            ],
            "columns": [
                {
                    "table": "Product",
                    "column": "ListPrice",
                    "score": 0.6,
                    "matched_terms": ["price"],
                    "reasons": ["token_column_match:price"]
                }, ...
            ]
        }
        """
        query_tokens = self._extract_query_tokens(query)
        tables = self.catalog.get_tables()

        column_results = []
        table_scores = {t: 0.0 for t in tables}
        table_matched_terms = {t: set() for t in tables}
        table_reasons = {t: [] for t in tables}

        # 1. Direct Table Scoring
        for table in tables:
            for q_tok in query_tokens:
                score, signal = self._evaluate_lexical_signal(q_tok, table)
                if score > 0:
                    table_scores[table] += score
                    table_matched_terms[table].add(q_tok["raw"])
                    table_reasons[table].append(f"{signal}_table_match:{q_tok['raw']}")

        # 2. Column Scoring & Evidence Propagation
        for table in tables:
            cols = self.catalog.get_columns(table)
            for col in cols:
                col_score = 0.0
                col_terms = set()
                col_reasons = []

                for q_tok in query_tokens:
                    score, signal = self._evaluate_lexical_signal(q_tok, col)
                    if score > 0:
                        col_score += score
                        col_terms.add(q_tok["raw"])
                        col_reasons.append(f"{signal}_column_match:{q_tok['raw']}")

                column_results.append({
                    "table": table,
                    "column": col,
                    "score": round(col_score, 3),
                    "matched_terms": list(col_terms),
                    "reasons": col_reasons
                })

                # Propagate column evidence boost to parent table if column matched
                if col_score > 0:
                    evidence_boost = COLUMN_EVIDENCE_WEIGHT
                    table_scores[table] += evidence_boost
                    table_matched_terms[table].update(col_terms)
                    table_reasons[table].append(f"column_evidence:{col}")

        # Format and sort table results
        table_results = []
        for table in tables:
            table_results.append({
                "table": table,
                "score": round(table_scores[table], 3),
                "matched_terms": list(table_matched_terms[table]),
                "reasons": table_reasons[table]
            })

        table_results.sort(key=lambda x: x["score"], reverse=True)
        column_results.sort(key=lambda x: x["score"], reverse=True)

        return {
            "tables": table_results,
            "columns": column_results
        }
