def bellman_ford(edges): # 1 indexed
    dist = [INF] * (n + 1)
    prec = [-1] * (n + 1)
    for _ in range(n):
        x = -1
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                prec[v] = u
                dist[v] = dist[u] + w
                x = v
    if x != -1:         # reconstruire cycle neg
        for _ in range(n):
            x = prec[x]
        end = x
        path = [x]
        while prec[x] != end:
            x = prec[x]
            path.append(x)
        path.append(end)
        return path[::-1]
    return []