# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.LamSlotWind import LamSlotWind

from pyleecan.Methods.Machine.LamSquirrelCage.build_geometry import build_geometry
from pyleecan.Methods.Machine.LamSquirrelCage.check import check
from pyleecan.Methods.Machine.LamSquirrelCage.comp_length_ring import comp_length_ring
from pyleecan.Methods.Machine.LamSquirrelCage.plot import plot

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Material import Material
from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.WindingCW1L import WindingCW1L
from pyleecan.Classes.WindingCW2LR import WindingCW2LR
from pyleecan.Classes.WindingCW2LT import WindingCW2LT
from pyleecan.Classes.WindingDW1L import WindingDW1L
from pyleecan.Classes.WindingDW2L import WindingDW2L
from pyleecan.Classes.WindingSC import WindingSC
from pyleecan.Classes.WindingUD import WindingUD
from pyleecan.Classes.Slot import Slot
from pyleecan.Classes.SlotMFlat import SlotMFlat
from pyleecan.Classes.SlotMPolar import SlotMPolar
from pyleecan.Classes.SlotW10 import SlotW10
from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.Classes.SlotW12 import SlotW12
from pyleecan.Classes.SlotW13 import SlotW13
from pyleecan.Classes.SlotW14 import SlotW14
from pyleecan.Classes.SlotW15 import SlotW15
from pyleecan.Classes.SlotW16 import SlotW16
from pyleecan.Classes.SlotW21 import SlotW21
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.Classes.SlotW23 import SlotW23
from pyleecan.Classes.SlotW24 import SlotW24
from pyleecan.Classes.SlotW25 import SlotW25
from pyleecan.Classes.SlotW26 import SlotW26
from pyleecan.Classes.SlotW27 import SlotW27
from pyleecan.Classes.SlotW28 import SlotW28
from pyleecan.Classes.SlotW29 import SlotW29
from pyleecan.Classes.SlotW60 import SlotW60
from pyleecan.Classes.SlotW61 import SlotW61
from pyleecan.Classes.Hole import Hole
from pyleecan.Classes.HoleMag import HoleMag
from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.HoleM51 import HoleM51
from pyleecan.Classes.HoleM52 import HoleM52
from pyleecan.Classes.HoleM53 import HoleM53
from pyleecan.Classes.HoleM54 import HoleM54
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Classes.VentilationTrap import VentilationTrap


class LamSquirrelCage(LamSlotWind):

    VERSION = 1

    # cf Methods.Machine.LamSquirrelCage.build_geometry
    build_geometry = build_geometry
    # cf Methods.Machine.LamSquirrelCage.check
    check = check
    # cf Methods.Machine.LamSquirrelCage.comp_length_ring
    comp_length_ring = comp_length_ring
    # cf Methods.Machine.LamSquirrelCage.plot
    plot = plot
    # save method is available in all object
    save = save

    def __init__(
        self,
        Hscr=0.03,
        Lscr=0.015,
        ring_mat=-1,
        Ksfill=None,
        winding=-1,
        slot=-1,
        L1=0.35,
        mat_type=-1,
        Nrvd=0,
        Wrvd=0,
        Kf1=0.95,
        is_internal=True,
        Rint=0,
        Rext=1,
        is_stator=True,
        axial_vent=list(),
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if ring_mat == -1:
            ring_mat = Material()
        if winding == -1:
            winding = Winding()
        if slot == -1:
            slot = Slot()
        if mat_type == -1:
            mat_type = Material()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(
                init_dict,
                [
                    "Hscr",
                    "Lscr",
                    "ring_mat",
                    "Ksfill",
                    "winding",
                    "slot",
                    "L1",
                    "mat_type",
                    "Nrvd",
                    "Wrvd",
                    "Kf1",
                    "is_internal",
                    "Rint",
                    "Rext",
                    "is_stator",
                    "axial_vent",
                ],
            )
            # Overwrite default value with init_dict content
            if "Hscr" in list(init_dict.keys()):
                Hscr = init_dict["Hscr"]
            if "Lscr" in list(init_dict.keys()):
                Lscr = init_dict["Lscr"]
            if "ring_mat" in list(init_dict.keys()):
                ring_mat = init_dict["ring_mat"]
            if "Ksfill" in list(init_dict.keys()):
                Ksfill = init_dict["Ksfill"]
            if "winding" in list(init_dict.keys()):
                winding = init_dict["winding"]
            if "slot" in list(init_dict.keys()):
                slot = init_dict["slot"]
            if "L1" in list(init_dict.keys()):
                L1 = init_dict["L1"]
            if "mat_type" in list(init_dict.keys()):
                mat_type = init_dict["mat_type"]
            if "Nrvd" in list(init_dict.keys()):
                Nrvd = init_dict["Nrvd"]
            if "Wrvd" in list(init_dict.keys()):
                Wrvd = init_dict["Wrvd"]
            if "Kf1" in list(init_dict.keys()):
                Kf1 = init_dict["Kf1"]
            if "is_internal" in list(init_dict.keys()):
                is_internal = init_dict["is_internal"]
            if "Rint" in list(init_dict.keys()):
                Rint = init_dict["Rint"]
            if "Rext" in list(init_dict.keys()):
                Rext = init_dict["Rext"]
            if "is_stator" in list(init_dict.keys()):
                is_stator = init_dict["is_stator"]
            if "axial_vent" in list(init_dict.keys()):
                axial_vent = init_dict["axial_vent"]
        # Initialisation by argument
        self.Hscr = Hscr
        self.Lscr = Lscr
        # ring_mat can be None, a Material object or a dict
        if isinstance(ring_mat, dict):
            self.ring_mat = Material(init_dict=ring_mat)
        else:
            self.ring_mat = ring_mat
        # Call LamSlotWind init
        super(LamSquirrelCage, self).__init__(
            Ksfill=Ksfill,
            winding=winding,
            slot=slot,
            L1=L1,
            mat_type=mat_type,
            Nrvd=Nrvd,
            Wrvd=Wrvd,
            Kf1=Kf1,
            is_internal=is_internal,
            Rint=Rint,
            Rext=Rext,
            is_stator=is_stator,
            axial_vent=axial_vent,
        )
        # The class is frozen (in LamSlotWind init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        LamSquirrelCage_str = ""
        # Get the properties inherited from LamSlotWind
        LamSquirrelCage_str += super(LamSquirrelCage, self).__str__() + linesep
        LamSquirrelCage_str += "Hscr = " + str(self.Hscr) + linesep
        LamSquirrelCage_str += "Lscr = " + str(self.Lscr) + linesep
        LamSquirrelCage_str += "ring_mat = " + str(self.ring_mat.as_dict())
        return LamSquirrelCage_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from LamSlotWind
        if not super(LamSquirrelCage, self).__eq__(other):
            return False
        if other.Hscr != self.Hscr:
            return False
        if other.Lscr != self.Lscr:
            return False
        if other.ring_mat != self.ring_mat:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from LamSlotWind
        LamSquirrelCage_dict = super(LamSquirrelCage, self).as_dict()
        LamSquirrelCage_dict["Hscr"] = self.Hscr
        LamSquirrelCage_dict["Lscr"] = self.Lscr
        if self.ring_mat is None:
            LamSquirrelCage_dict["ring_mat"] = None
        else:
            LamSquirrelCage_dict["ring_mat"] = self.ring_mat.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        LamSquirrelCage_dict["__class__"] = "LamSquirrelCage"
        return LamSquirrelCage_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Hscr = None
        self.Lscr = None
        if self.ring_mat is not None:
            self.ring_mat._set_None()
        # Set to None the properties inherited from LamSlotWind
        super(LamSquirrelCage, self)._set_None()

    def _get_Hscr(self):
        """getter of Hscr"""
        return self._Hscr

    def _set_Hscr(self, value):
        """setter of Hscr"""
        check_var("Hscr", value, "float", Vmin=0)
        self._Hscr = value

    # short circuit ring section radial height [m]
    # Type : float, min = 0
    Hscr = property(
        fget=_get_Hscr,
        fset=_set_Hscr,
        doc=u"""short circuit ring section radial height [m]""",
    )

    def _get_Lscr(self):
        """getter of Lscr"""
        return self._Lscr

    def _set_Lscr(self, value):
        """setter of Lscr"""
        check_var("Lscr", value, "float", Vmin=0)
        self._Lscr = value

    # short circuit ring section axial length
    # Type : float, min = 0
    Lscr = property(
        fget=_get_Lscr,
        fset=_set_Lscr,
        doc=u"""short circuit ring section axial length""",
    )

    def _get_ring_mat(self):
        """getter of ring_mat"""
        return self._ring_mat

    def _set_ring_mat(self, value):
        """setter of ring_mat"""
        check_var("ring_mat", value, "Material")
        self._ring_mat = value

        if self._ring_mat is not None:
            self._ring_mat.parent = self

    # Material of the Rotor short circuit ring
    # Type : Material
    ring_mat = property(
        fget=_get_ring_mat,
        fset=_set_ring_mat,
        doc=u"""Material of the Rotor short circuit ring""",
    )
