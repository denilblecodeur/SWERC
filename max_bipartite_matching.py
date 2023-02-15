# Petites instances ~10^3
def max_bipartite_matching(bigraph, n, m):
    def augment(u):
        if visit[u]:
            return False
        visit[u] = True
        for v in bigraph[u]:
            if matching[v] == -1 or augment(matching[v]):
                matching[v] = u
                return True
        return False
    matching = [-1] * (n + m)
    for u in range(n):
        visit = [False] * n
        augment(u)
    return matching

# Grandes instances ~10^5
class BipartiteMatching:
    def __init__(self, n, m):
        self._n = n
        self._m = m
        self._to = [[] for _ in range(n)]

    def add_edge(self, a, b):
        self._to[a].append(b)

    def solve(self):
        n, m, to = self._n, self._m, self._to
        prev = [-1] * n
        root = [-1] * n
        p = [-1] * n
        q = [-1] * m
        updated = True
        while updated:
            updated = False
            s = []
            s_front = 0
            for i in range(n):
                if p[i] == -1:
                    root[i] = i
                    s.append(i)
            while s_front < len(s):
                v = s[s_front]
                s_front += 1
                if p[root[v]] != -1:
                    continue
                for u in to[v]:
                    if q[u] == -1:
                        while u != -1:
                            q[u] = v
                            p[v], u = u, p[v]
                            v = prev[v]
                        updated = True
                        break
                    u = q[u]
                    if prev[u] != -1:
                        continue
                    prev[u] = v
                    root[u] = root[v]
                    s.append(u)
            if updated:
                for i in range(n):
                    prev[i] = -1
                    root[i] = -1
        return [(v, p[v]) for v in range(n) if p[v] != -1]

n, m, k = map(int, input().split())
bm = BipartiteMatching(n, m)
for _ in range(k):
    a, b = map(int, input().split())
    bm.add_edge(a - 1, b - 1)
ans = bm.solve()
print(len(ans))
for a, b in ans:
    print(a + 1, b + 1)

"""Minimum vertex cover"""
def _alternate(u, bigraph, visitU, visitV, matchV):
    """extend alternating tree from free vertex u.
      visitU, visitV marks all vertices covered by the tree.
    """
    visitU[u] = True
    for v in bigraph[u]:
        if not visitV[v]:
            visitV[v] = True
            assert matchV[v] is not None  # otherwise match is not maximum
            _alternate(matchV[v], bigraph, visitU, visitV, matchV)


def bipartite_vertex_cover(bigraph):
    """Bipartite minimum vertex cover by Koenig's theorem
    Selected vertices form a minimum vertex cover,
    i.e. every edge is adjacent to at least one selected vertex
    and number of selected vertices is minimum"""
    V = range(len(bigraph))
    matchV = max_bipartite_matching(bigraph)
    matchU = [None for u in V]
    for v in V:                      # -- build the mapping from U to V
        if matchV[v] is not None:
            matchU[matchV[v]] = v
    visitU = [False for u in V]      # -- build max alternating forest
    visitV = [False for v in V]
    for u in V:
        if matchU[u] is None:        # -- starting with free vertices in U
            _alternate(u, bigraph, visitU, visitV, matchV)
    inverse = [not b for b in visitU]
    return (inverse, visitV)