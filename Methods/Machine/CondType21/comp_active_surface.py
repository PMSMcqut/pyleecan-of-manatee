# -*- coding: utf-8 -*-
"""@package Methods.Machine.CondType21.comp_active_surface
Conductor Type 2_1 comp_active_surface method
@date Created on Mon Jan 12 17:20:56 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_active_surface(self):
    """Compute the active surface of the conductor

    Parameters
    ----------
    self : CondType21
        A CondType21 object

    Returns
    -------
    Sact: float
        Surface without insulation [m**2]

    """

    Sact = self.Hbar * self.Wbar

    return Sact
