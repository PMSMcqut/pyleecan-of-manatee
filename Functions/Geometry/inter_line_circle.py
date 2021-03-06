# -*- coding: utf-8 -*-
"""@package inter_line_circle
@date Created on mars 16 09:58 2018
@author pierre_b
"""
from numpy import sqrt


def inter_line_circle(Z1, Z2, R):
    """INTER_LINE_CIRCLE find the intersection between a circle of center(0, 0)
    and radius r with a line defined by two points

    Parameters
    ----------
    Z1 : complex
        Complex coordinate of a point on the line

    Z2 : complex
        Complex coordinate of another point on the line
    R : float
        Radius of the circle [m]

    Returns
    -------
    Zlist: list
        List of the complex coordinates of the intersection
    """
    x1 = Z1.real
    y1 = Z1.imag
    x2 = Z2.real
    y2 = Z2.imag

    dx = x2 - x1
    dy = y2 - y1
    dr = sqrt(dx ** 2 + dy ** 2)
    D = x1 * y2 - x2 * y1

    delta = R ** 2 * dr ** 2 - D ** 2
    if delta < 0:  # 0 point
        return list()
    elif delta == 0:  # 1 point(tangent)
        return [(D * dy - 1j * D * dx) / dr ** 2]
    else:  # 2 points
        if dy < 0:
            xs1 = (D * dy - dx * sqrt(delta)) / dr ** 2
            xs2 = (D * dy + dx * sqrt(delta)) / dr ** 2
        else:
            xs1 = (D * dy + dx * sqrt(delta)) / dr ** 2
            xs2 = (D * dy - dx * sqrt(delta)) / dr ** 2
        ys1 = (-D * dx + abs(dy) * sqrt(delta)) / dr ** 2
        ys2 = (-D * dx - abs(dy) * sqrt(delta)) / dr ** 2

        return [xs1 + 1j * ys1, xs2 + 1j * ys2]
