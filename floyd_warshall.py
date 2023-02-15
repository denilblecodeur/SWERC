def idx(i, j, dim):
    return i + j * dim
def floyd_warshall(n, distances):     
    for k in range(n):
        for i in range(n):
            d1 = distances[idx(i, k, n)]
            if k != i and d1 != INF:
                for j in range(i):
                    t = d1 + distances[idx(k, j, n)]
                    if t < distances[idx(i, j, n)]:
                        distances[idx(i, j, n)] = distances[idx(j, i, n)] = t
    return distances