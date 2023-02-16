def multigraphEulerian(graph, src=0):
    def cycle(adj, s):
        start = s
        choosen = -1
        C = [start]
        while choosen != start:
            choosen = graph[s][0]
            C.append(choosen)
            graph[s].remove(choosen)
            graph[choosen].remove(s)
            s = choosen
        return C
    def fusion(C1, C2):
        u = C1.index(C2[0])
        return C1[:u] + C2 + C1[u + 1:]
    C = cycle(graph, src)
    while len(toVisit:=[v for v in C if len(graph[v]) > 0]) > 0:
        C = fusion(C, cycle(graph, toVisit[src]))
    return C