def augment(graph, capacity, flow, source, target):
    n = len(graph)
    A = [0] * n
    augm_path = [None] * n
    Q = deque([source])
    augm_path[source] = source
    A[source] = 1<<59
    while Q:
        u = Q.popleft()
        for v in graph[u]:
            cuv = capacity[u][v]
            residual = cuv - flow[u][v]
            if residual > 0 and augm_path[v] is None:
                augm_path[v] = u
                A[v] = min(A[u], residual)
                if v == target:
                    break
                else:
                    Q.append(v)
    return (augm_path, A[target])

def edmonds_karp(graph, capacity, source, target):
    add_reverse_arcs(graph, capacity)
    V = range(len(graph))
    flow = [[0] * V for _ in range(V)]
    while True:
        augm_path, delta = augment(graph, capacity, flow, source, target)
        if delta == 0:
            break
        v = target
        while v != source:
            u = augm_path[v]
            flow[u][v] += delta
            flow[v][u] -= delta
            v = u
    return (flow, sum(flow[source]))
