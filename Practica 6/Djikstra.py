import heapq

grafo = {
    0: [(1, 9), (4, 6)],
    1: [(0, 9), (3, 8)],
    2: [(5, 6), (4, 5)],
    3: [(1, 8), (5, 1), (7, 7)],
    4: [(0, 6), (2, 5), (6, 3)],
    5: [(3, 1), (2, 6)],
    6: [(4, 3), (7, 2)],
    7: [(3, 7), (6, 2)]
}

def dijkstra(grafo, inicio):
    dist = {nodo: float("inf") for nodo in grafo}
    dist[inicio] = 0

    prev = {nodo: None for nodo in grafo}

    pq = [(0, inicio)]  # (distancia, nodo)

    while pq:
        distancia_actual, nodo_actual = heapq.heappop(pq)

        if distancia_actual > dist[nodo_actual]:
            continue

        for vecino, peso in grafo[nodo_actual]:
            nueva_dist = distancia_actual + peso

            if nueva_dist < dist[vecino]:
                dist[vecino] = nueva_dist
                prev[vecino] = nodo_actual
                heapq.heappush(pq, (nueva_dist, vecino))

    return dist, prev

def reconstruir_camino(prev, destino):
    camino = []
    while destino is not None:
        camino.append(destino)
        destino = prev[destino]
    return camino[::-1]


# EJEMPLO: desde nodo 0
inicio = 0
distancias, previos = dijkstra(grafo, inicio)

print("Distancias desde", inicio)
for nodo in distancias:
    print(f"{inicio} -> {nodo} = {distancias[nodo]}")

# Camino más corto de 0 a 7
destino = 7
camino = reconstruir_camino(previos, destino)
print("\nCamino más corto de 0 a 7:", camino)
print("Costo:", distancias[destino])