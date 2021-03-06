# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.Winding import Winding

from pyleecan.Methods.Machine.WindingDW2L.comp_connection_mat import comp_connection_mat
from pyleecan.Methods.Machine.WindingDW2L.get_dim_wind import get_dim_wind

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Conductor import Conductor
from pyleecan.Classes.CondType11 import CondType11
from pyleecan.Classes.CondType12 import CondType12
from pyleecan.Classes.CondType21 import CondType21
from pyleecan.Classes.CondType22 import CondType22


class WindingDW2L(Winding):
    """double layer overlapping integral distributed winding, radial coil superposition """

    VERSION = 1

    # cf Methods.Machine.WindingDW2L.comp_connection_mat
    comp_connection_mat = comp_connection_mat
    # cf Methods.Machine.WindingDW2L.get_dim_wind
    get_dim_wind = get_dim_wind
    # save method is available in all object
    save = save

    def __init__(
        self,
        coil_pitch=5,
        is_reverse_wind=False,
        Nslot_shift_wind=0,
        qs=3,
        Ntcoil=7,
        Npcpp=2,
        type_connection=0,
        p=3,
        Lewout=0.015,
        conductor=-1,
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if conductor == -1:
            conductor = Conductor()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(
                init_dict,
                [
                    "coil_pitch",
                    "is_reverse_wind",
                    "Nslot_shift_wind",
                    "qs",
                    "Ntcoil",
                    "Npcpp",
                    "type_connection",
                    "p",
                    "Lewout",
                    "conductor",
                ],
            )
            # Overwrite default value with init_dict content
            if "coil_pitch" in list(init_dict.keys()):
                coil_pitch = init_dict["coil_pitch"]
            if "is_reverse_wind" in list(init_dict.keys()):
                is_reverse_wind = init_dict["is_reverse_wind"]
            if "Nslot_shift_wind" in list(init_dict.keys()):
                Nslot_shift_wind = init_dict["Nslot_shift_wind"]
            if "qs" in list(init_dict.keys()):
                qs = init_dict["qs"]
            if "Ntcoil" in list(init_dict.keys()):
                Ntcoil = init_dict["Ntcoil"]
            if "Npcpp" in list(init_dict.keys()):
                Npcpp = init_dict["Npcpp"]
            if "type_connection" in list(init_dict.keys()):
                type_connection = init_dict["type_connection"]
            if "p" in list(init_dict.keys()):
                p = init_dict["p"]
            if "Lewout" in list(init_dict.keys()):
                Lewout = init_dict["Lewout"]
            if "conductor" in list(init_dict.keys()):
                conductor = init_dict["conductor"]
        # Initialisation by argument
        self.coil_pitch = coil_pitch
        # Call Winding init
        super(WindingDW2L, self).__init__(
            is_reverse_wind=is_reverse_wind,
            Nslot_shift_wind=Nslot_shift_wind,
            qs=qs,
            Ntcoil=Ntcoil,
            Npcpp=Npcpp,
            type_connection=type_connection,
            p=p,
            Lewout=Lewout,
            conductor=conductor,
        )
        # The class is frozen (in Winding init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        WindingDW2L_str = ""
        # Get the properties inherited from Winding
        WindingDW2L_str += super(WindingDW2L, self).__str__() + linesep
        WindingDW2L_str += "coil_pitch = " + str(self.coil_pitch)
        return WindingDW2L_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Winding
        if not super(WindingDW2L, self).__eq__(other):
            return False
        if other.coil_pitch != self.coil_pitch:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Winding
        WindingDW2L_dict = super(WindingDW2L, self).as_dict()
        WindingDW2L_dict["coil_pitch"] = self.coil_pitch
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        WindingDW2L_dict["__class__"] = "WindingDW2L"
        return WindingDW2L_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.coil_pitch = None
        # Set to None the properties inherited from Winding
        super(WindingDW2L, self)._set_None()

    def _get_coil_pitch(self):
        """getter of coil_pitch"""
        return self._coil_pitch

    def _set_coil_pitch(self, value):
        """setter of coil_pitch"""
        check_var("coil_pitch", value, "int", Vmin=0, Vmax=1000)
        self._coil_pitch = value

    # winding coil pitch or coil span expressed in slots (coil_pitch1=Zs/(2p)->full-pitch distributed winding, coil_pitch1<Zs/(2p)->chorded/shorted-pitch distributed winding, coil_pitch1=1->tooth-winding). Coil pitch is sometimes written 1/9 means Input.Magnetics.coil_pitch1=9-1=8
    # Type : int, min = 0, max = 1000
    coil_pitch = property(
        fget=_get_coil_pitch,
        fset=_set_coil_pitch,
        doc=u"""winding coil pitch or coil span expressed in slots (coil_pitch1=Zs/(2p)->full-pitch distributed winding, coil_pitch1<Zs/(2p)->chorded/shorted-pitch distributed winding, coil_pitch1=1->tooth-winding). Coil pitch is sometimes written 1/9 means Input.Magnetics.coil_pitch1=9-1=8""",
    )
