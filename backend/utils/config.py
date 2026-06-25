from pathlib import Path

MODEL_NAME = "qwen2.5"
DATABASE_LANGUAGE = "SQLite"

_backend_root = Path(__file__).resolve().parents[1]
_primary_db = _backend_root / "AdventureWorks-sqlite.db"
_fallback_db = _backend_root / "api" / "AdventureWorks-sqlite.db"

if _primary_db.exists() and _primary_db.stat().st_size > 0:
    DB_PATH = str(_primary_db)
elif _fallback_db.exists() and _fallback_db.stat().st_size > 0:
    DB_PATH = str(_fallback_db)
else:
    DB_PATH = str(_primary_db)
