import math

adj_list = {
    "a": {"b": 2, "d": 8},
    "b": {"a": 2, "d": 5, "e": 6},
    "c": {"e": 9, "f": 3},
    "d": {"a": 8, "b": 5, "e": 3, "f": 2},
    "e": {"b": 6, "d": 3, "f": 1, "c": 9},
    "f": {"d": 2, "e": 1, "c": 3},
}

adj_list = {
    "s": {"a": 1, "b": 4, "c": 2},
    "a": {"d": 5, "e": 6},
    "b": {"d": 8, "f": 3},
    "c": {"g": 3},
    "d": {"h": 2},
    "e": {"h": 4},
    "f": {"i": 7},
    "g": {"i": 4},
    "h": {"j": 5},
    "i": {"j": 3},
    "j": {},
}


def dijkstra(start: str, adjacency_list):
    my_dict = {}
    for key in adjacency_list:
        distance = 0 if key == start else math.inf
        my_dict[key] = {"distance": distance, "prev": None}

    seen = set()
    queue = [start]

    while queue:
        shortest = math.inf
        idx = None
        for i, v in enumerate(queue):
            dist = my_dict[v]["distance"]
            if dist < shortest:
                shortest = dist
                idx = i

        curr_node = queue.pop(idx)
        if curr_node in seen:
            continue

        curr_distance = my_dict[curr_node]["distance"]

        for neighbor, distance in adjacency_list[curr_node].items():
            # check how far we are from each
            new_distance = curr_distance + distance
            if new_distance < my_dict[neighbor]["distance"]:
                my_dict[neighbor]["distance"] = new_distance
                my_dict[neighbor]["prev"] = curr_node

            queue.append(neighbor)

            seen.add(curr_node)

    for node, val in my_dict.items():
        print(node, val)


dijkstra("s", adj_list)

print("done")
