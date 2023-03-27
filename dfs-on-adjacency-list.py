adj_list = {}

adj_list["A"] = {"label": "Vertex A", "neighbors": ["B", "C", "D"]}
adj_list["B"] = {"label": "Vertex B", "neighbors": ["A", "C", "E"]}
adj_list["C"] = {"label": "Vertex C", "neighbors": ["A", "B", "D", "E", "F"]}
adj_list["D"] = {"label": "Vertex D", "neighbors": ["A", "C", "E"]}
adj_list["E"] = {"label": "Vertex E", "neighbors": ["B", "C", "D", "F"]}
adj_list["F"] = {"label": "Vertex F", "neighbors": ["C", "E"]}


def search(vertex_list, seen, vertex_name, target) -> bool:
    if vertex_name in seen:
        return False

    seen.add(vertex_name)

    vertex = vertex_list[vertex_name]
    if vertex["label"] == target:
        return True

    for neighbor_name in vertex["neighbors"]:
        if search(vertex_list, seen, neighbor_name, target):
            return True

    return False


# not shortest path, just path
def search_path(vertex_list, seen, vertex_name, target) -> list[str]:
    if vertex_name in seen:
        return []

    seen.add(vertex_name)

    vertex = vertex_list[vertex_name]
    if vertex["label"] == target:
        return [vertex_name]

    for neighbor_name in vertex["neighbors"]:
        res = search_path(vertex_list, seen, neighbor_name, target)
        if res:
            return [vertex_name] + res

    return []


print(search(adj_list, set(), "A", "Vertex A"))
print(search(adj_list, set(), "A", "Vertex R"))
print(search(adj_list, set(), "A", "Vertex F"))

print("--")

print(search_path(adj_list, set(), "A", "Vertex A"))
print(search_path(adj_list, set(), "A", "Vertex R"))
print(search_path(adj_list, set(), "A", "Vertex F"))
print(search_path(adj_list, set(), "A", "Vertex E"))
