# -*- coding: utf-8 -*-
"""@package Methods.Machine.Winding._comp_wind_type_2
Compute the Winding Matrix (for type 2) Method
@date Created on Mon Dec 15 16:04:48 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import array, power, zeros

from pyleecan.Methods.Machine.Winding import WindingError
from pyleecan.Functions.Winding.reverse_wind_mat import reverse_wind_mat
from pyleecan.Functions.Winding.shift_wind_mat import shift_wind_mat


def comp_connection_mat(self, Zs):
    """Compute the Winding Matrix (for winding type 2)
    type 2 : TOOTH WINDING, SINGLE LAYER ALTERNATE TEETH WOUND
    (Nlay_rad=1,Nlay_tan=1)

    Parameters
    ----------
    self : Winding
        A: Winding object
    Zs : int
        Number of Slot (Integer >0)

    Returns
    -------
    wind_mat: numpy.ndarray
        Winding Matrix (1, 1, Zs, qs)

    Raises
    ------
    WindingT2DefNtError
        Zs/qs/2 must be an integer

    """

    assert Zs > 0, "Zs must be >0"
    assert Zs % 1 == 0, "Zs must be an integer"

    # non overlapping ALTERNATE TEETH WOUND-> single layer
    # cf "2D exact analytical model for surface-mounted permanent-magnet motors
    # with semi-closed slots" -> U motor 10p/18s creates 2p, Zs/2+2p, Zs/2-2p

    qs = self.qs  # Phase Number
    Nt = Zs / float(qs) / 2.0  # Number of teeth by semi phase

    # Ncspc= Zs/(2.0*qs*self.Npcpp/nlay)  # number of coils in series per parallel circuit
    # Ntspc = self.Ntcoil * Ncspc #Number of turns in series per phase
    Ntcoil = self.Ntcoil  # number of turns per coils

    if round(Nt) != Nt:  # Nt must be an integer
        raise WindingT2DefNtError(
            "wrong winding definition, cannot wind all "
            "the teeth (Zs/qs/2 is not an integer)!"
        )

    # first strategy - checked with Umbra_08 motor and Umbra_05: the winding
    # direction of each tooth is reversed
    wind_mat = zeros((1, 1, Zs, qs))

    for k in range(0, int(Nt)):  # winding alternatively the teeth
        for q in range(0, qs):
            xenc = q * 2 + k * 2 * qs + array([1, 2])
            wind_mat[0][0][int((xenc[0] - 1) % Zs)][q] = (
                power(-1, xenc[0] + q + k + 1) * Ntcoil
            )
            wind_mat[0][0][(xenc[1] - 1) % Zs][q] = (
                power(-1, xenc[1] + q + k + 1) * Ntcoil
            )

    # Apply the transformations
    if self.is_reverse_wind:
        wind_mat = reverse_wind_mat(wind_mat)
    if self.Nslot_shift_wind > 0:
        wind_mat = shift_wind_mat(wind_mat, self.Nslot_shift_wind)

    return wind_mat


class WindingT2DefNtError(WindingError):
    """ """

    pass
