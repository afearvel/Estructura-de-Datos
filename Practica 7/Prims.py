def prim(graph, start):
    visited = [False] * len(graph)
    visited[start] = True

    mst = []
    total = 0

    for _ in range(len(graph) - 1):
        min_weight = float('inf')
        u = -1
        v = -1

        # buscar la arista más barata que conecte
        # un nodo visitado con uno no visitado
        for i in range(len(graph)):
            if visited[i]:
                for neighbor, weight in graph[i]:
                    if not visited[neighbor] and weight < min_weight:
                        min_weight = weight
                        u = i
                        v = neighbor

        visited[v] = True
        mst.append((u, v, min_weight))
        total += min_weight

    return mst, total


graph = {
    0: [(2, 20), (1, 10)],
    1: [(0, 10), (3, 50), (4, 10)],
    2: [(0, 20), (3, 20), (4, 33)],
    3: [(1, 50), (2, 20), (4, 20), (5, 2)],
    4: [(1, 10), (2, 33), (3, 20), (5, 1)],
    5: [(4, 1), (3, 2)]
}

mst, total = prim(graph, 2)

print("MST:")
for u, v, w in mst:
    print(f"nodo {u} a nodo {v} costo: {w}")

print("Costo total:", total)