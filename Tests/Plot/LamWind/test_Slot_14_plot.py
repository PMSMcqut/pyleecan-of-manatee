# -*- coding: utf-8 -*-
"""
@date Created on Tue Jan 12 13:54:56 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from os.path import join
from unittest import TestCase

import matplotlib.pyplot as plt
from numpy import array, pi, zeros

from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.LamSquirrelCage import LamSquirrelCage
from pyleecan.Classes.Machine import Machine
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Classes.VentilationTrap import VentilationTrap
from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.WindingUD import WindingUD
from pyleecan.Classes.WindingCW2LT import WindingCW2LT
from pyleecan.Classes.WindingDW2L import WindingDW2L
from pyleecan.Classes.BHCurveMat import BHCurveMat
from pyleecan.Classes.BHCurveParam import BHCurveParam
from pyleecan.Classes.MatLamination import MatLamination
from pyleecan.Classes.SlotW14 import SlotW14

from pyleecan.Tests.Plot import save_path
from pyleecan.Tests.Plot.LamWind import wind_mat


class test_Lam_Wind_14_plot(TestCase):
    """unittest for Lamination with winding plot"""

    def test_Lam_Wind_14_wind_22(self):
        """Test machine plot with Slot 14 and winding rad=2, tan=2
		"""
        print("\nTest plot Slot 14")
        plt.close("all")
        test_obj = Machine()
        test_obj.rotor = LamSlotWind(
            Rint=0.2,
            Rext=0.5,
            is_internal=True,
            is_stator=False,
            L1=0.95,
            Nrvd=1,
            Wrvd=0.05,
        )
        test_obj.rotor.slot = SlotW14(
            Zs=6, W0=100e-3, W3=200e-3, H0=15e-3, H1=25e-3, H3=140e-3
        )
        test_obj.rotor.winding = WindingUD(
            user_wind_mat=wind_mat, qs=4, p=4, Lewout=60e-3
        )
        test_obj.shaft = Shaft(Drsh=test_obj.rotor.Rint * 2, Lshaft=1)
        test_obj.shaft.mat_type.name = "M270_35A"

        test_obj.rotor.mat_type.name = "Load_M400"
        test_obj.rotor.mat_type.magnetics = MatLamination(Wlam=0.5e-3)

        test_obj.stator = LamSlotWind(
            Rint=0.51,
            Rext=1,
            is_internal=False,
            is_stator=True,
            L1=0.95,
            Nrvd=1,
            Wrvd=0.05,
        )
        test_obj.stator.slot = SlotW14(
            Zs=6, W0=100e-3, W3=200e-3, H0=15e-3, H1=25e-3, H3=140e-3
        )
        test_obj.stator.winding = WindingUD(
            user_wind_mat=wind_mat, qs=4, p=4, Lewout=60e-3
        )
        test_obj.stator.mat_type.name = "Param"
        test_obj.stator.mat_type.magnetics = MatLamination(Wlam=0.5e-3)
        BH = BHCurveParam(Bmax=1.5, mur_0=8585, mur_1=21.79, a=0.25575)
        test_obj.stator.mat_type.magnetics.BH_curve = BH

        test_obj.frame = Frame(Rint=1, Rext=1.1, Lfra=1)
        test_obj.frame.mat_type.name = "M330_35A"

        test_obj.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s14_1-Machine.png"))
        # Rotor + Stator + 2 for frame + 1 for shaft
        self.assertEqual(len(fig.axes[0].patches), 55)

        test_obj.rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s14_2-Rotor.png"))
        # 2 for lam + Zs*4 for wind
        self.assertEqual(len(fig.axes[0].patches), 26)

        test_obj.stator.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Wind_s14_3-Stator.png"))
        # 2 for lam + Zs*4 for wind
        self.assertEqual(len(fig.axes[0].patches), 26)
