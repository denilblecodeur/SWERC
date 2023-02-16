def great_circle_distance(radius, point_A, point_B):
    long_a, lat_a = map(math.radians, point_A)
    long_b, lat_b = map(math.radians, point_B)
    return radius * math.acos(
        math.cos(lat_a) * math.cos(lat_b) * math.cos(abs(long_a - long_b))
        + math.sin(lat_a) * math.sin(lat_b))