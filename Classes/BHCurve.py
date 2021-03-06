# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Methods.Material.BHCurve.plot import plot

from pyleecan.Classes.check import InitUnKnowClassError


class BHCurve(FrozenClass):
    """Abstract B(H) curve class"""

    VERSION = 1

    # cf Methods.Material.BHCurve.plot
    plot = plot
    # save method is available in all object
    save = save

    def __init__(self, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, [])
        # The class is frozen, for now it's impossible to add new properties
        self.parent = None
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        BHCurve_str = ""
        if self.parent is None:
            BHCurve_str += "parent = None " + linesep
        else:
            BHCurve_str += "parent = " + str(type(self.parent)) + " object" + linesep
        return BHCurve_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        BHCurve_dict = dict()
        # The class name is added to the dict fordeserialisation purpose
        BHCurve_dict["__class__"] = "BHCurve"
        return BHCurve_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""
