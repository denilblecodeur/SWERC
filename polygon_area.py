def polygon_area(p):
    area = exterior = 0
    for i in range(n):
        area += p[i - 1][0] * p[i][1] - p[i][0] * p[i - 1][1]
        X = abs(p[i - 1][0] - p[i][0])
        Y = abs(p[i - 1][1] - p[i][1])
        if X == 0:
            exterior += Y
        elif Y == 0:
            exterior += X
        else:
            exterior += gcd(X, Y)
    area = abs(area / 2)
    interior = area - exterior / 2 + 1
    return area, exterior, (abs(area) - exterior + 2)//2