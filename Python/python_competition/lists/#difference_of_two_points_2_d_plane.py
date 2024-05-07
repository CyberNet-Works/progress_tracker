#difference_of_two_points_2_d_plane
import math
def calculate_distance(point1, point2):
    x2 = point1[0]
    x1 = point2[0]
    y1 = point1[1]
    y2 = point2[1]


    return "{:.1f}".format((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** .5)