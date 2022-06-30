import math


def paint_and_value(wall_square_meter):
    liter_of_paint = wall_square_meter / 3
    gallon_of_paint = math.ceil(liter_of_paint / 18)
    return gallon_of_paint, gallon_of_paint * 80


print(paint_and_value(180))
