def get_projete(xa, ya, xb, yb, xm, ym):
    vertical = xa == xb
    if vertical:
        return xa, ym
    else:
        a = (yb - ya) / (xb - xa)
        b = yb - xb * a
        xu, yu = xb - xa, yb - ya
        xh = (xm * xu + ym * yu - b * yu) / (xu + a * yu)
        yh = a * xh + b
        return xh, yh