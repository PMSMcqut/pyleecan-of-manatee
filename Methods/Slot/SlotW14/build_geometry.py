# -*- coding: utf-8 -*-
"""@package

@date Created on Thu Mar 30 14:30:21 2017
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""

from pyleecan.Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve (Segment) needed to plot the Slot.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotW14
        A SlotW14 object

    Returns
    -------
    curve_list: list
        A list of 8 Segment

    """

    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9] = self._comp_point_coordinate()
    # Creation of curve
    curve_list = list()
    if self.H0 > 0:
        curve_list.append(Segment(Z1, Z2))
    curve_list.append(Segment(Z2, Z3))
    curve_list.append(Segment(Z3, Z4))
    curve_list.append(Segment(Z4, Z5))
    curve_list.append(Segment(Z5, Z6))
    curve_list.append(Segment(Z6, Z7))
    curve_list.append(Segment(Z7, Z8))
    if self.H0 > 0:
        curve_list.append(Segment(Z8, Z9))

    return curve_list
