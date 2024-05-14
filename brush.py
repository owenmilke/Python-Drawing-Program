import pygame

pygame.init()


def brush(screen_, brush_color_, x_, y_, brush_size_):
    """
    :param screen_: Canvas for brush to draw on
    :param brush_color_: Color of brush
    :param x_: x-coordinate of brush
    :param y_: y-coordinate of brush
    :param brush_size_: Size of brush
    :return: Allows the user to draw a line with varying color and size
    """
    pygame.draw.circle(screen_, brush_color_, (x_, y_), brush_size_)
