# vérifier tout sommet degré pair
def eulerian_tour_undirected(n, m, graph):
    Q = [0]
    path = []
    while Q:
        node = Q[-1]
        visited[node] = True
        if len(graph[node]) == 0:
            path.append(Q.pop())
            continue
        neigh = graph[node].pop()
        graph[neigh].remove(node)   # Graph is list of sets
        Q.append(neigh)
    return path if len(path) == m + 1 and all(visited) else -1
