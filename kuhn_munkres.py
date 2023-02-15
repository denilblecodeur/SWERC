"""Couplage parfait de profit maximal en O(|U|^2 * |V|)
 - si minimal, changer signe des poids
 - si |U| > |V|, ajouter sommets à V reliés à
   tous les sommets de U par un poids 0
 - si graph non complet, le compléter avec arêtes
   de poids -inf
"""
def kuhn_munkres(G, TOLERANCE=1e-6):
    """
    G: weight matrix where G[u][v] is the weight of edge (u,v),
    TOLERANCE: a value with absolute value below tolerance
               is considered as being zero.
               If G consists of integer or fractional values
               then TOLERANCE can be chosen 0.
    graph (U,V,E) is complete bi-partite graph with len(U) <= len(V)
        float('-inf') or float('inf') entries in G
        are allowed but not None.
    returns matching table from U to V, value of matching
    """
    nU = len(G)
    U = range(nU)
    nV = len(G[0])
    V = range(nV)
    assert nU <= nV
    mu = [None] * nU                # empty matching
    mv = [None] * nV
    lu = [max(row) for row in G]    # trivial labels
    lv = [0] * nV
    for root in U:                  # build an alternate tree
        au = [False] * nU           # au, av mark nodes...
        au[root] = True             # ... covered by the tree
        Av = [None] * nV            # Av[v] successor of v in the tree
        # for every vertex u, slack[u] := (val, v) such that
        # val is the smallest slack on the constraints (*)
        # with fixed u and v being the corresponding vertex
        slack = [(lu[root] + lv[v] - G[root][v], root) for v in V]
        while True:
            (delta, u), v = min((slack[v], v) for v in V if Av[v] is None)
            assert au[u]
            if delta > TOLERANCE:   # tree is full
                for u0 in U:        # improve labels
                    if au[u0]:
                        lu[u0] -= delta
                for v0 in V:
                    if Av[v0] is not None:
                        lv[v0] += delta
                    else:
                        (val, arg) = slack[v0]
                        slack[v0] = (val - delta, arg)
            assert abs(lu[u] + lv[v] - G[u][v]) <= TOLERANCE  # equality
            Av[v] = u                # add (u, v) to A
            if mv[v] is None:
                break                # alternating path found
            u1 = mv[v]
            assert not au[u1]
            au[u1] = True            # add (u1, v) to A
            for v1 in V:
                if Av[v1] is None:   # update margins
                    alt = (lu[u1] + lv[v1] - G[u1][v1], u1)
                    if slack[v1] > alt:
                        slack[v1] = alt
        while v is not None:         # ... alternating path found
            u = Av[v]                # along path to root
            prec = mu[u]
            mv[v] = u                # augment matching
            mu[u] = v
            v = prec
    return (mu, sum(lu) + sum(lv))