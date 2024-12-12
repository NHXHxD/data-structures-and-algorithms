def bellman_ford(vertices, edges, source):

    dist = [float('inf')] * vertices
    dist[source] = 0

    for i in range(vertices - 1):
        for (u, v, w) in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist