import math
def color_difference(color1, color2):
    x2 = color2[0]
    x1 = color1[0]
    y2 = color2[1]
    y1 = color1[1]
    z2 = color2[2]
    z1 = color1[2]

#    return color1, x1, y1, z1, color2, x2, y2, z2
 
    result = "{:.2f}".format(((x2 - x1) **2 + (y2 - y1) ** 2 + (z2 - z1) **2) ** .5)
    return result