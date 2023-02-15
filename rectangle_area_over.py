def rectangle_area_over((ax1, ay1), (ax2, ay2), (bx1, by1), (bx2, by2)):
    # ax1, ay1 = bottom-left
    # ax2, ay2 = top-right
    x_over = max(min(ax2,bx2) - max(ax1,bx1),0)
    y_over = max(min(ay2,by2) - max(ay1,by1),0)

    is_x_over = max(ax1, bx1) < min(ax2, bx2)
    is_y_over = max(ay1, by1) < min(ay2, by2)