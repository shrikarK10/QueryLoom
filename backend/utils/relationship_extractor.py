from collections import defaultdict, deque
def extract_relationships(connector):
    """
    Extracts relationships from the database.
    """
    

    relationships = []

    tables = connector.execute_query(
        "SELECT name FROM sqlite_master WHERE type='table';"
    )

    for (table_name,) in tables:
        fk_info = connector.execute_query(f"PRAGMA foreign_key_list({table_name});")

        for fk in fk_info:
            relationships.append({
                "from_table": table_name,
                "from_column": fk[3],
                "to_table": fk[2],
                "to_column": fk[4]
            })

    return relationships



def build_relationship_graph(relationships):
    """
    Builds a relationship graph from the extracted relationships.
    """
    graph = defaultdict(list)

    for rel in relationships:
        a = rel["from_table"]
        b = rel["to_table"]

        graph[a].append(b)
        graph[b].append(a)

    return graph


import heapq

def find_join_path(graph, start, end):
    """
    Finds the join path of least weight between two tables using Dijkstra's algorithm.
    """
    queue = [(0, [start])]
    visited = {}

    def get_edge_weight(t1, t2):
        bridge_tables = {"customeraddress", "productmodelproductdescription"}
        if t1.lower() in bridge_tables or t2.lower() in bridge_tables:
            return 5
        return 1

    while queue:
        weight, path = heapq.heappop(queue)
        node = path[-1]

        if node == end:
            return path

        if node in visited and visited[node] <= weight:
            continue
        visited[node] = weight

        for neighbor in graph[node]:
            edge_wt = get_edge_weight(node, neighbor)
            new_weight = weight + edge_wt
            if neighbor not in visited or new_weight < visited.get(neighbor, float('inf')):
                heapq.heappush(queue, (new_weight, path + [neighbor]))

    return None


def build_joins(path, relationships):
    """
    Convert join path to SQL JOIN
    """
    joins = []

    for i in range(len(path) - 1):
        t1 = path[i]
        t2 = path[i + 1]

        for rel in relationships:
            if rel["from_table"] == t1 and rel["to_table"] == t2:
                joins.append(
                    f"JOIN {t2} ON {t1}.{rel['from_column']} = {t2}.{rel['to_column']}"
                )
                break

            elif rel["from_table"] == t2 and rel["to_table"] == t1:
                joins.append(
                    f"JOIN {t2} ON {t2}.{rel['from_column']} = {t1}.{rel['to_column']}"
                )
                break

    return "\n".join(joins)