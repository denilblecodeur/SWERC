from heapq import heappush, heappop
def topological_order(graph, indeg):
    Q = [node for node in range(len(graph)) if indeg[node] == 0]
    order = []
    while Q:
        node = heappop(Q)
        order.append(node + 1)
        for neigh in graph[node]:
            indeg[neigh] -= 1
            if indeg[neigh] == 0:
                heappush(Q, neigh)
    return order