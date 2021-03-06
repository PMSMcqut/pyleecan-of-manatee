# -*- coding: utf-8 -*-
from matplotlib.patches import Polygon

from pyleecan.Methods.Machine import PATCH_COLOR, PATCH_EDGE


def get_patch(self, color=PATCH_COLOR, edgecolor=PATCH_EDGE):
    """Returns the Trapeze Patch to be display in matplotlib

    Parameters
    ----------
    self : Trapeze
        a Trapeze object

    color :
        the color of the patch (Default value = PATCH_COLOR)
    edgecolor :
        the color of the patch's edges (Default value = PATCH_EDGE)

    Returns
    -------
    patch : matplotlib.patches.Polygon
        The patch corresponding to the surface

    """
    # check if the Trapeze is correct*
    self.check()

    line_list = self.get_lines()
    Z_list = list()
    # For each Line discretize
    for line in line_list:
        Z_list.extend(list(line.discretize()))

    # abscissa coordinate
    Zr_list = list()
    # ordinate coordinate
    Zi_list = list()

    for ii in range(len(Z_list)):
        Zr_list.append(Z_list[ii].real)
        Zi_list.append(Z_list[ii].imag)
    point_list = list(zip(Zr_list, Zi_list))
    return Polygon(point_list, closed=True, facecolor=color, edgecolor=edgecolor)
