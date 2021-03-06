# -*- coding: utf-8 -*-
"""@package build_geometry
@date Created on juin 20 11:12 2018
@author franco_i
"""
from numpy import pi, angle, exp

from pyleecan.Classes.Circle import Circle
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Segment import Segment


def build_geometry(self, sym=1, alpha=0, delta=0):
    """Build the geometry of the LamSlot object

    Parameters
    ----------
    self : LamSlot
        a LamSlot object
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation

    Returns
    -------
    surf_list : list
        list of surfaces needed to draw the lamination

    """

    # getting Number of Slot
    Zs = self.slot.Zs

    # Check for symmetry
    assert (Zs % sym) == 0

    if self.is_stator:
        ll = "Stator"  # Label lamination
    else:
        ll = "Rotor"
    if self.is_internal:
        ls = "Ext"  # label for the slot
        ly = "In"  # label for the yoke
    else:
        ls = "In"
        ly = "Ext"

    Ryoke = self.get_Ryoke()
    slot_pitch = 2 * pi / Zs
    op_angle = self.slot.comp_angle_opening()
    t_angle = slot_pitch - op_angle
    H_yoke = self.comp_height_yoke()

    # getting the Lines that delimit one slot
    Slot_lines = self.slot.build_geometry()
    for line in Slot_lines:
        line.rotate(slot_pitch / 2)
    # getting the bore line
    bore_lines = self.get_bore_line(slot_pitch - t_angle / 2, slot_pitch + t_angle / 2)
    Slot_lines.extend(bore_lines)

    # Generate all the Bore lines
    line_list = list()
    for ii in range(Zs // sym):
        # Duplicate and rotate the slot + bore for each slot
        for line in Slot_lines:
            new_line = type(line)(init_dict=line.as_dict())
            new_line.rotate(ii * slot_pitch)
            line_list.append(new_line)

    # Create the lamination surface(s)
    surf_list = list()
    if sym == 1:  # Complete lamination
        # Create Slot surface
        surf_slot = SurfLine(
            line_list=line_list,
            label="Lamination_" + ll + "_bore_" + ls,
            point_ref=None,
        )
        # Create yoke circle surface
        if Ryoke > 0:
            surf_yoke = Circle(
                radius=Ryoke,
                label="Lamination_" + ll + "_yoke_" + ly,
                point_ref=Ryoke - (H_yoke / 2),
                center=0,
            )
        # The order matters when plotting
        if self.is_internal:
            surf_list.append(surf_slot)
            if Ryoke > 0:
                surf_list.append(surf_yoke)
        else:
            if Ryoke > 0:
                surf_list.append(surf_yoke)
            surf_list.append(surf_slot)
    else:  # Only one surface
        # Modify the bore radius
        if len(bore_lines) > 0:
            line_list.pop(-1)
            start_angle = angle(line_list[-1].get_end())
            line_list.extend(
                self.get_bore_line(
                    start_angle,
                    start_angle + t_angle / 2,
                    label="Bore_line",
                    is_half=True,
                )
            )
            line_list.insert(
                0,
                self.get_bore_line(0, t_angle / 2, label="Bore_line", is_half=True)[0],
            )
        # Add the Yoke part
        Zy1 = Ryoke
        Zy2 = Ryoke * exp(1j * 2 * pi / sym)
        line_list.append(Segment(line_list[-1].get_end(), Zy2, label=ll + "_Yoke_side"))
        if Ryoke > 0:  # For internal lamination
            line_list.append(Arc1(Zy2, Zy1, -Ryoke, ll + "_Yoke_Radius"))
        line_list.append(
            Segment(Zy1, line_list[0].get_begin(), label=ll + "_Yoke_side")
        )
        # Create a Surface for the slot
        surf_slot = SurfLine(
            line_list=line_list, label="Lamination_" + ll + "_bore_Ext", point_ref=None
        )
        surf_list.append(surf_slot)

    # Apply the transformations
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    # Adding the ventilation surfaces
    for vent in self.axial_vent:
        surf_list += vent.build_geometry(
            sym=sym, alpha=alpha, delta=delta, is_stator=self.is_stator
        )
    return surf_list
