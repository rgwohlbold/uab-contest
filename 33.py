#!/usr/bin/python3

def build(start, words, graph):
    level = len(start)
    chars = []

    for i in range(len(words) - 1):
        graph[words[i][level]] = words[i+1][level]
        chars.append(words[i+1][level])

    for char in chars:
        charlist = list(filter(lambda x: len(x) > level and x[level] == char, words))
        build(start + char, charlist, graph)

    return graph


# Topological sorting algorithm
def kahn(graph):
    # The result list
    result = []
    # How many incoming edges does a vertex have
    in_degree = {}

    # Add keys
    for k in graph.keys():
        in_degree[k] = 0
    # Add values
    for k, v in graph.items():
        for i in v:
            if i not in in_degree:
                in_degree[i] = 1
            else:
                in_degree[i] += 1

    # Contains vertices with no incoming edges
    alone = {v for v, count in in_degree.items() if count == 0}

    # If alone is empty, no other connection was found
    while len(alone) != 0:
        # Remove a node that has no incoming vertices from the graph
        node = alone.pop()
        # And add it to the result list
        result.append(node)
        # Remove the edges to all neighbors
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            # Add neighbor to the alone set if they don't have any other incoming vertices
            if in_degree[neighbor] == 0:
                alone.add(neighbor)

    # No DAG exists
    if len(result) != len(in_degree):
        return None

    return result




l = ["AB", "AC", "BE", "BD", "BA"]
graph = build("", l, {})
print(kahn(graph))
