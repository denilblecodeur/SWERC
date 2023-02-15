def _dinic_step(lev, u, target, limit):
    if limit <= 0:
        return 0
    if u == target:
        return limit
    val = 0
    for v in graph[u]:
        residuel = graph[u][v] - flow[u][v]
        if lev[v] == lev[u] + 1 and residuel > 0:
            z = min(limit, residuel)
            aug = _dinic_step(lev, v, target, z)
            flow[u][v] += aug
            flow[v][u] -= aug
            val += aug
            limit -= aug
    if val == 0:
        lev[u] = None
    return val

def get_min_cut(n, source, target, graph):
    Q = deque()
    total = 0
    flow = [[0] * n for _ in range(n)]
    while True:
        Q.appendleft(source)
        lev = [None] * n
        lev[source] = 0
        while Q:
            u = Q.pop()
            for v in graph[u]:
                if lev[v] is None and graph[u][v] > flow[u][v]:
                    lev[v] = lev[u] + 1
                    Q.appendleft(v)
        if lev[target] is None:
            break
        UB = sum(graph[source][v] for v in graph[source]) - total
        total += _dinic_step(lev, source, target, UB, flow, graph)

    reachable = set([source])
    Q = [source]
    seen = set()
    while Q:
        u = Q.pop()
        seen.add(u)
        for v in graph[u]:
            if v not in seen and graph[u][v] > flow[u][v]:
                reachable.add(v)
                Q.append(v)
    cut = []
    for u in reachable:
        for v in graph[u]:
            if v not in reachable:
                cut.append((u + 1, v + 1))
    return cut

n, m = map(int, input().split())
source, target = 0, n - 1
graph = [{} for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    if u == v:
        continue
    if v - 1 not in graph[u - 1]:
        graph[u - 1][v - 1] = 0
        graph[v - 1][u - 1] = 0
    graph[u - 1][v - 1] += w
    graph[v - 1][u - 1] += w
    #add reverse edge with weight 0, or w if edge is bidirectionnal