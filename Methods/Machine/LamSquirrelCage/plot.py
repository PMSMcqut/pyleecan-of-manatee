# -*- coding: utf-8 -*-
"""@package Methods.Machine.LamSquirrelCage.plot
LamSquirrelCage plot method
@date Created on Tue Jan 27 13:53:39 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from matplotlib.patches import Patch, Polygon, Wedge
from matplotlib.pyplot import axis, legend
from numpy import array, exp, pi

from pyleecan.Functions.init_fig import init_fig
from pyleecan.Methods.Machine import BAR_COLOR, SCR_COLOR


def plot(self, fig=None, plot_winding=False, sym=1, alpha=0, delta=0):
    """Plot the Lamination in a matplotlib fig

    Parameters
    ----------
    self : LamSquirrelCage
        A LamSquirrelCage object
    fig :
        if None, open a new fig and plot, else add to the current
        one (Default value = None)
    plot_winding : bool
        If true, plot the bar and short circuit ring (Default value = False)
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation

    Returns
    -------
    None
    """

    # Lamination and ventilation ducts patches
    (fig, axes, patch_leg, label_leg) = init_fig(fig)
    # Plot the lamination
    super(type(self), self).plot(
        fig, plot_winding=False, sym=sym, alpha=alpha, delta=delta
    )

    # Plot the winding if needed
    if plot_winding:
        # point needed to plot the bar of a slot
        Hbar = self.winding.conductor.Hbar
        Wbar = self.winding.conductor.Wbar
        if self.is_internal:
            HS = self.Rext - self.slot.comp_height(self.Rext)
            Bar_points = [
                HS + 1j * Wbar / 2,
                HS - 1j * Wbar / 2,
                HS + Hbar - 1j * Wbar / 2,
                HS + Hbar + 1j * Wbar / 2,
            ]
        else:
            HS = self.Rint + self.slot.comp_height(self.Rint)
            Bar_points = [
                HS + 1j * Wbar / 2,
                HS - 1j * Wbar / 2,
                HS - Hbar - 1j * Wbar / 2,
                HS - Hbar + 1j * Wbar / 2,
            ]
        Bar_array = array(Bar_points)
        # Computation of the coordinate of every bar by complex rotation
        bar_list = []
        for i in range(self.slot.Zs):
            bar_list.append(Bar_array * exp(-1j * i * (2 * pi) / self.slot.Zs))

        patches = list()
        # Creation of the bar patches
        for wind in bar_list:
            patches.append(Polygon(zip(wind.real, wind.imag), color=BAR_COLOR))

        # Add the Short Circuit Ring
        if self.is_internal:
            Rmw = self.slot.comp_radius_mid_wind(self.Rext)
        else:
            Rmw = self.slot.comp_radius_mid_wind(self.Rint)
        patches.append(
            Wedge(
                (0, 0), Rmw + self.Hscr / 2.0, 0, 360, width=self.Hscr, color=SCR_COLOR
            )
        )  # Full ring

    # Display the result
    axes.set_xlabel("(m)")
    axes.set_ylabel("(m)")
    axes.set_title("Squirrel Cage Rotor")

    # Axis Setup
    axis("equal")
    Lim = self.Rext * 1.5
    axes.set_xlim(-Lim, Lim)
    axes.set_ylim(-Lim, Lim)

    if plot_winding:
        # Add the magnet to the fig
        for patch in patches:
            axes.add_patch(patch)
        # Legend setup (Rotor already setup by LamSlotWind.plot)
        patch_leg.append(Patch(color=BAR_COLOR))
        label_leg.append("Rotor Bar")
        patch_leg.append(Patch(color=SCR_COLOR))
        label_leg.append("Short Circuit Ring")

        legend(patch_leg, label_leg)
    fig.show()
