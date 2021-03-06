# -*- coding: utf-8 -*-
"""@package Methods.Machine.Magnet_Type_2.comp_surface
Compute the Magnet surface method
@date Created on Wed Dec 17 16:06:11 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""
from numpy import pi


def comp_surface(self):
    """Compute the Magnet surface (by numerical computation)

    Parameters
    ----------
    self : MagnetType11
        A MagnetType11 object

    Returns
    -------
    S: float
        Magnet surface [m**2]

    """

    [Z1, Z2, Z3, Zs3, Zs4, Z4, Zref] = self._comp_point_coordinate()
    Rslot = abs(Z1)
    Rtop = abs(Z3)

    if self.is_outwards():
        S = pi * (Rslot ** 2 - Rtop ** 2)
    else:
        S = pi * (Rtop ** 2 - Rslot ** 2)
    return S * self.Wmag / (2 * pi)
