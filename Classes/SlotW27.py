# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.SlotWind import SlotWind

from pyleecan.Methods.Slot.SlotW27._comp_point_coordinate import _comp_point_coordinate
from pyleecan.Methods.Slot.SlotW27.build_geometry import build_geometry
from pyleecan.Methods.Slot.SlotW27.build_geometry_wind import build_geometry_wind
from pyleecan.Methods.Slot.SlotW27.check import check
from pyleecan.Methods.Slot.SlotW27.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.SlotW27.comp_height import comp_height
from pyleecan.Methods.Slot.SlotW27.comp_height_wind import comp_height_wind
from pyleecan.Methods.Slot.SlotW27.comp_surface import comp_surface
from pyleecan.Methods.Slot.SlotW27.comp_surface_wind import comp_surface_wind

from pyleecan.Classes.check import InitUnKnowClassError


class SlotW27(SlotWind):
    """semi-closed trapezoidal without fillet without wedge (flat bottom)"""

    VERSION = 1
    IS_SYMMETRICAL = 1

    # cf Methods.Slot.SlotW27._comp_point_coordinate
    _comp_point_coordinate = _comp_point_coordinate
    # cf Methods.Slot.SlotW27.build_geometry
    build_geometry = build_geometry
    # cf Methods.Slot.SlotW27.build_geometry_wind
    build_geometry_wind = build_geometry_wind
    # cf Methods.Slot.SlotW27.check
    check = check
    # cf Methods.Slot.SlotW27.comp_angle_opening
    comp_angle_opening = comp_angle_opening
    # cf Methods.Slot.SlotW27.comp_height
    comp_height = comp_height
    # cf Methods.Slot.SlotW27.comp_height_wind
    comp_height_wind = comp_height_wind
    # cf Methods.Slot.SlotW27.comp_surface
    comp_surface = comp_surface
    # cf Methods.Slot.SlotW27.comp_surface_wind
    comp_surface_wind = comp_surface_wind
    # save method is available in all object
    save = save

    def __init__(
        self,
        H0=0.003,
        H1=0,
        H2=0.02,
        W0=0.003,
        W1=0.013,
        W2=0.01,
        W3=0.003,
        is_trap_wind=False,
        Zs=36,
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(
                init_dict,
                ["H0", "H1", "H2", "W0", "W1", "W2", "W3", "is_trap_wind", "Zs"],
            )
            # Overwrite default value with init_dict content
            if "H0" in list(init_dict.keys()):
                H0 = init_dict["H0"]
            if "H1" in list(init_dict.keys()):
                H1 = init_dict["H1"]
            if "H2" in list(init_dict.keys()):
                H2 = init_dict["H2"]
            if "W0" in list(init_dict.keys()):
                W0 = init_dict["W0"]
            if "W1" in list(init_dict.keys()):
                W1 = init_dict["W1"]
            if "W2" in list(init_dict.keys()):
                W2 = init_dict["W2"]
            if "W3" in list(init_dict.keys()):
                W3 = init_dict["W3"]
            if "is_trap_wind" in list(init_dict.keys()):
                is_trap_wind = init_dict["is_trap_wind"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
        # Initialisation by argument
        self.H0 = H0
        self.H1 = H1
        self.H2 = H2
        self.W0 = W0
        self.W1 = W1
        self.W2 = W2
        self.W3 = W3
        self.is_trap_wind = is_trap_wind
        # Call SlotWind init
        super(SlotW27, self).__init__(Zs=Zs)
        # The class is frozen (in SlotWind init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        SlotW27_str = ""
        # Get the properties inherited from SlotWind
        SlotW27_str += super(SlotW27, self).__str__() + linesep
        SlotW27_str += "H0 = " + str(self.H0) + linesep
        SlotW27_str += "H1 = " + str(self.H1) + linesep
        SlotW27_str += "H2 = " + str(self.H2) + linesep
        SlotW27_str += "W0 = " + str(self.W0) + linesep
        SlotW27_str += "W1 = " + str(self.W1) + linesep
        SlotW27_str += "W2 = " + str(self.W2) + linesep
        SlotW27_str += "W3 = " + str(self.W3) + linesep
        SlotW27_str += "is_trap_wind = " + str(self.is_trap_wind)
        return SlotW27_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from SlotWind
        if not super(SlotW27, self).__eq__(other):
            return False
        if other.H0 != self.H0:
            return False
        if other.H1 != self.H1:
            return False
        if other.H2 != self.H2:
            return False
        if other.W0 != self.W0:
            return False
        if other.W1 != self.W1:
            return False
        if other.W2 != self.W2:
            return False
        if other.W3 != self.W3:
            return False
        if other.is_trap_wind != self.is_trap_wind:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from SlotWind
        SlotW27_dict = super(SlotW27, self).as_dict()
        SlotW27_dict["H0"] = self.H0
        SlotW27_dict["H1"] = self.H1
        SlotW27_dict["H2"] = self.H2
        SlotW27_dict["W0"] = self.W0
        SlotW27_dict["W1"] = self.W1
        SlotW27_dict["W2"] = self.W2
        SlotW27_dict["W3"] = self.W3
        SlotW27_dict["is_trap_wind"] = self.is_trap_wind
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SlotW27_dict["__class__"] = "SlotW27"
        return SlotW27_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.H0 = None
        self.H1 = None
        self.H2 = None
        self.W0 = None
        self.W1 = None
        self.W2 = None
        self.W3 = None
        self.is_trap_wind = None
        # Set to None the properties inherited from SlotWind
        super(SlotW27, self)._set_None()

    def _get_H0(self):
        """getter of H0"""
        return self._H0

    def _set_H0(self, value):
        """setter of H0"""
        check_var("H0", value, "float", Vmin=0)
        self._H0 = value

    # Slot isthmus height.
    # Type : float, min = 0
    H0 = property(fget=_get_H0, fset=_set_H0, doc=u"""Slot isthmus height.""")

    def _get_H1(self):
        """getter of H1"""
        return self._H1

    def _set_H1(self, value):
        """setter of H1"""
        check_var("H1", value, "float", Vmin=0)
        self._H1 = value

    # Slot first part height
    # Type : float, min = 0
    H1 = property(fget=_get_H1, fset=_set_H1, doc=u"""Slot first part height""")

    def _get_H2(self):
        """getter of H2"""
        return self._H2

    def _set_H2(self, value):
        """setter of H2"""
        check_var("H2", value, "float", Vmin=0)
        self._H2 = value

    # Slot second part height
    # Type : float, min = 0
    H2 = property(fget=_get_H2, fset=_set_H2, doc=u"""Slot second part height""")

    def _get_W0(self):
        """getter of W0"""
        return self._W0

    def _set_W0(self, value):
        """setter of W0"""
        check_var("W0", value, "float", Vmin=0)
        self._W0 = value

    # Slot isthmus width.
    # Type : float, min = 0
    W0 = property(fget=_get_W0, fset=_set_W0, doc=u"""Slot isthmus width.""")

    def _get_W1(self):
        """getter of W1"""
        return self._W1

    def _set_W1(self, value):
        """setter of W1"""
        check_var("W1", value, "float", Vmin=0)
        self._W1 = value

    # Slot top width.
    # Type : float, min = 0
    W1 = property(fget=_get_W1, fset=_set_W1, doc=u"""Slot top width.""")

    def _get_W2(self):
        """getter of W2"""
        return self._W2

    def _set_W2(self, value):
        """setter of W2"""
        check_var("W2", value, "float", Vmin=0)
        self._W2 = value

    # Slot middle width
    # Type : float, min = 0
    W2 = property(fget=_get_W2, fset=_set_W2, doc=u"""Slot middle width""")

    def _get_W3(self):
        """getter of W3"""
        return self._W3

    def _set_W3(self, value):
        """setter of W3"""
        check_var("W3", value, "float", Vmin=0)
        self._W3 = value

    # Slot bottom width.
    # Type : float, min = 0
    W3 = property(fget=_get_W3, fset=_set_W3, doc=u"""Slot bottom width.""")

    def _get_is_trap_wind(self):
        """getter of is_trap_wind"""
        return self._is_trap_wind

    def _set_is_trap_wind(self, value):
        """setter of is_trap_wind"""
        check_var("is_trap_wind", value, "bool")
        self._is_trap_wind = value

    # If True, split the winding on the  trapezium bases. Else split at the middle height as usual
    # Type : bool
    is_trap_wind = property(
        fget=_get_is_trap_wind,
        fset=_set_is_trap_wind,
        doc=u"""If True, split the winding on the  trapezium bases. Else split at the middle height as usual""",
    )
