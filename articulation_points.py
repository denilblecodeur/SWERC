def cut_nodes_edges(graph):
    n = len(graph)
    time = 0
    num = [None] * n
    low = [n] * n
    father = [None] * n
    critical_childs = [0] * n
    times_seen = [-1] * n
    for start in range(n):
        if times_seen[start] == -1:
            times_seen[start] = 0
            to_visit = [start]
            while to_visit:
                node = to_visit[-1]
                if times_seen[node] == 0:
                    num[node] = time
                    time += 1
                    low[node] = float('inf')
                children = graph[node]
                if times_seen[node] == len(children):
                    to_visit.pop()
                    up = father[node]
                    if up is not None:
                        low[up] = min(low[up], low[node])
                        if low[node] >= num[up]:
                            critical_childs[up] += 1
                else:
                    child = children[times_seen[node]]
                    times_seen[node] += 1
                    if times_seen[child] == -1:
                        father[child] = node
                        times_seen[child] = 0
                        to_visit.append(child)
                    elif num[child] < num[node] and father[node] != child:
                        low[node] = min(low[node], num[child])
    cut_edges = []
    cut_nodes = []
    for node in range(n):
        if father[node] == None:
            if critical_childs[node] >= 2:
                cut_nodes.append(node)
        else:
            if critical_childs[node] >= 1:
                cut_nodes.append(node)
            if low[node] >= num[node]:
                cut_edges.append((father[node], node))
    return cut_nodes, cut_edges