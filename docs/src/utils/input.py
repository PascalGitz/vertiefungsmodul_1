import os

## Pfad anpassen
workspace_dir = "C:/Users/Pascal Gitz/OneDrive - Hochschule Luzern/02_Master/03_Tragverhalten_von_Stahlbetontragwerken"
os.chdir(workspace_dir)

## Sympy und Hilfsfunktionen
import sympy as sp
from sympy.abc import *
from sympycalcs import param_value, dict_render, dict_to_table, eq_pretty_units, eq_subs
import sympy.physics.units as unit


## Unit definitions


# Kräfte
setattr(unit, "kilonewton", unit.Quantity("kilonewton", abbrev="kN", is_prefixed=True))
setattr(unit, "kN", getattr(unit, "kilonewton"))
getattr(unit, "kilonewton").set_global_relative_scale_factor(unit.kilo, unit.newton)
sp.init_printing(use_latex="mathjax", latex_mode="equation", mat_symbol_style="bold")

## Numerische Berechnungen

import numpy as np
import scipy.integrate as integrate
import astropy.units as un

## Plotting und display

import matplotlib.pyplot as plt
from docs.src.utils.plotstyle import set_engineering_style  # Plotstyle

set_engineering_style()
from IPython.display import Markdown  # Für Tabellen

## Pfad um Import von src zu vereinfachen
import sys

sys.path.append("../")


## Printing

from IPython.display import Latex, Markdown


# SYMPY SYMBOLE

# Symbole für Zustandslinien Biegeträger
EI, F_A, F_B, F_C, f_B, f_A, f_C = sp.symbols("EI F_A F_B F_C f_B, f_A, f_C")
c_1, c_2, c_3, c_4 = sp.symbols("c_1:5", real=True)
a_1, a_2, a_3, a_4, a_5 = sp.symbols("a_1:6", positive=True)
b_auflager, l_tot = sp.symbols("b_Auflager l_tot", positive=True)
q_x = sp.Function("q")(x)
M_x = sp.Function("M")(x)
V_x = sp.Function("V")(x)
w_x = sp.Function("w")(x)
phi_x = sp.Function("varphi")(x)

# Analogieträger Mohr
q_x_a = sp.Function("q_a")(x)
M_x_a = sp.Function("M_a")(x)
V_x_a = sp.Function("V_a")(x)
w_x_a = sp.Function("w_a")(x)
phi_x_a = sp.Function("varphi_a")(x)

chi_M = sp.Function("chi")(M)


# Symbole für Integration der Krümmung
E_c, E_s, EI_I, EI_II, EI_III = sp.symbols("E_c, E_s, EI^I, EI^{II},  EI^{III}")
d_1, d_2 = sp.symbols("d_1:3")
diam_s, diam_s_1, diam_s_2 = sp.symbols("\\oslash_s \\oslash_s\,1 \\oslash_s\,2")
z_1, z_2, z_3, z_4, z_5 = sp.symbols("z_1:6")
x_1, x_2, x_3, x_4, x_5 = sp.symbols("x_1:6")
W_c = sp.symbols("W_c")
w_1, w_1_gerissen_norm = sp.symbols("w_1 w_1_II\,SIA")
M_r, M_y, M_y_1, M_y_2, M_R, M_2 = sp.symbols("M_r, M_y, M_y_1, M_y_2, M_R, M_2")

V_R_s = sp.symbols("V_R\,s")
f_ct, f_cc, f_c, f_sy_1, f_sy_2, f_sy, f_su, f_su_1, f_su_2 = sp.symbols(
    "f_ct f_cc f_c f_sy\,1 f_sy\,2 f_sy f_su f_su\,1 f_su\,2"
)
A_i, A_c, A_s, A_s_1, A_s_2, A_sw = sp.symbols("A_i, A_c, A_s , A_s_1, A_s_2, A_s_w")
I_1, I_2 = sp.symbols("I^I I^{II}")

chi_r, chi_y, chi_y1, chi_y2, chi_II, chi_u = sp.symbols(
    "\chi_r, \chi_y, \chi_y1, \chi_y2, \chi^{II}, \chi_u"
)
s_x, s_w = sp.symbols("s_x s_w")
theta_c3, theta_c3_min, zeta_c, c_nom = sp.symbols(
    "theta_c3 theta_c3\,min zeta_c c_nom"
)


F_s1, F_s2, F_s3, F_s4, F_s5 = sp.symbols("F_s\,1:6")
F_s11, F_s21, F_s31, F_s41, F_s51 = sp.symbols("F_s1:6\,1")
F_s12, F_s22, F_s32, F_s42, F_s52 = sp.symbols("F_s1:6\,2")
F_c1, F_c2, F_c3, F_c4, F_c5 = sp.symbols("F_c\,1:6")


sigma_c_1, sigma_c_2, sigma_c_3, sigma_c_4, sigma_c_inf_5 = sp.symbols("sigma_c_1:6")
# sigma_c_11, sigma_c_21, sigma_c_31, sigma_c_41, sigma_c_inf_51 = sp.symbols('sigma_c_1:6\,1')
# sigma_c_12, sigma_c_22, sigma_c_32, sigma_c_42, sigma_c_inf_52 = sp.symbols('sigma_c_1:6\,2')

sigma_s_1, sigma_s_2, sigma_s_3, sigma_s_4, sigma_s_inf_5 = sp.symbols("sigma_s_1:6")
sigma_s_11, sigma_s_21, sigma_s_31, sigma_s_41, sigma_s_inf_51 = sp.symbols(
    "sigma_s_1:6\,1"
)
sigma_s_12, sigma_s_22, sigma_s_32, sigma_s_42, sigma_s_inf_52 = sp.symbols(
    "sigma_s_1:6\,2"
)

epsilon_s1, epsilon_s2, epsilon_s3, epsilon_s4, epsilon_s5 = sp.symbols(
    "varepsilon_s1:6"
)
epsilon_s11, epsilon_s21, epsilon_s31, epsilon_s41, epsilon_s51 = sp.symbols(
    "varepsilon_s1:6\,1"
)
epsilon_s12, epsilon_s22, epsilon_s32, epsilon_s42, epsilon_s52 = sp.symbols(
    "varepsilon_s1:6\,2"
)

epsilon_c1, epsilon_c2, epsilon_c3, epsilon_c4, epsilon_c5 = sp.symbols(
    "varepsilon_c\,1:6"
)
epsilon_sy, epsilon_cu, epsilon_su, epsilon_s, epsilon_c = sp.symbols(
    "varepsilon_sy varepsilon_cu varepsilon_su varepsilon_s varepsilon_c"
)

sigma_sy, sigma_cu, sigma_su, sigma_sr, sigma_sr0 = sp.symbols(
    "sigma_sy sigma_cu sigma_su sigma_sr sigma_sr0"
)

sigma_epsilon_s = sp.Function("sigma_s")(epsilon_s)
sigma_epsilon_c = sp.Function("sigma_c")(epsilon_c)


# Symbole für Zugversteifung
(
    lamb,
    rho_eff,
    s_rm,
    w_r,
) = sp.symbols("lambda rho_eff s_rm w_r")
delta_chi = sp.Function("\Delta\\chi")(lamb)


# Speichern der Gleichungen in einer Liste zum substituieren
Eq_list = []


def load_params_SV14():
    params_krummung = {
        # f_ct:4.*unit.N / unit.mm**2,
        # E_c:30000.*unit.N / unit.mm**2,
        E_s: 205000.0 * unit.N / unit.mm**2,
        diam_s_1: 18.0 * unit.mm,
        diam_s_2: 12.0 * unit.mm,
        c_nom: 35.0 * unit.mm,
        f_sy_1: 670.0 * unit.N / unit.mm**2,
        f_sy_2: 550.0 * unit.N / unit.mm**2,
        f_su_1: 800.0 * unit.N / unit.mm**2,
        f_su_2: 657.0 * unit.N / unit.mm**2,
        f_cc: 46.7 * unit.N / unit.mm**2,
        epsilon_cu: 3 / 1000,
        epsilon_su: 50 / 1000,
        theta_c3: 30.0,  # Degrees
    }

    params_zustandslinien = {
        b_auflager: 100 * unit.mm,  # Auflagerbreite
        a_1: 0.2 * unit.m,  # Abstand Auflager A vom Nullpunkt
        a_2: 1.5 * unit.m,  # Abstand Auflager A bis Einwirkung 1
        a_3: 1.0 * unit.m,  # Abstand Einwirkung 1 bis Einwirkung 2
        a_4: 1.5 * unit.m,  # Abstand Einwirkung 2 bis Auflager B
        a_5: 0.2 * unit.m,  # Abstand Auflager 2 bis Endpunkt
        b: 170.0 * unit.mm,  # Breite des Balkens
        h: 450.0 * unit.mm,  # Höhe des Balkens
    }

    Laststufen = np.linspace(1, 105 * 10**3, 100)

    return params_krummung, params_zustandslinien, Laststufen


def load_params_A3():
    # Versuch A3V2

    params_krummung = {
        # f_ct:4.*unit.N / unit.mm**2,
        # E_c:37700.*unit.N / unit.mm**2,
        E_s: 200000.0 * unit.N / unit.mm**2,
        s_x: 80.0 * unit.mm,
        diam_s: 12.0 * unit.mm,
        c_nom: 20.0 * unit.mm,
        f_sy: 546.0 * unit.N / unit.mm**2,
        f_su: 630.3 * unit.N / unit.mm**2,
        f_cc: 58.8 * unit.N / unit.mm**2,
        epsilon_cu: 5 / 1000,
        epsilon_su: 111.7 / 1000,
        theta_c3: 30.0,  # Degrees

    }

    params_zustandslinien = {
        b_auflager: 100 * unit.mm,  # Auflagerbreite
        a_1: 0.11 * unit.m,  # abstand zu A von 0
        a_2: 0.64 * unit.m,  # abstand von A zu C
        a_3: 0.92 * unit.m,  # abstand von C zu B
        a_4: 0.95 * unit.m,  # abstand von B zu D
        b: 800.0 * unit.mm,  # Breite des Trägers
        h: 200.0 * unit.mm,  # Höhe des Trägers,
    }

    Laststufen = np.linspace(1, 320 * 10**3, 100)

    return params_krummung, params_zustandslinien, Laststufen


def load_params_skript_Qs():
    # Beispielnachrechnung Spathelf Skript QS-Analyse

    params_krummung = {
        f_ct: 2.42 * unit.N / unit.mm**2,
        E_c: 32000.0 * unit.N / unit.mm**2,
        E_s: 205000.0 * unit.N / unit.mm**2,
        s_x: 120 * unit.mm,
        diam_s: 14.0 * unit.mm,
        c_nom: 30.0 * unit.mm,
        f_sy: 435.0 * unit.N / unit.mm**2,
        f_su: 435.0 * unit.N / unit.mm**2,
        f_cc: 16.5 * unit.N / unit.mm**2,
        epsilon_cu: 3 / 1000,
        epsilon_su: 45 / 1000,
    }

    params_zustandslinien = {
        b_auflager: 100 * unit.mm,  # Auflagerbreite
        a_1: 0.11 * unit.m,  # abstand zu A von 0
        a_2: 0.64 * unit.m,  # abstand von A zu C
        a_3: 0.92 * unit.m,  # abstand von C zu B
        a_4: 0.95 * unit.m,  # abstand von B zu D
        b: 300.0 * unit.mm,
        h: 450.0 * unit.mm,
    }

    Laststufen = np.linspace(1, 320 * 10**3, 100)

    return params_krummung, params_zustandslinien, Laststufen


def load_params_A5():
    # Versuch A5V2

    params_krummung = {
        f_ct: 3.62 * unit.N / unit.mm**2,
        E_c: 36100.0 * unit.N / unit.mm**2,
        E_s: 200000.0 * unit.N / unit.mm**2,
        s_x: 120.0 * unit.mm,
        diam_s: 12.0 * unit.mm,
        c_nom: 20.0 * unit.mm,
        f_sy: 500.0 * unit.N / unit.mm**2,
        f_cc: 63.3 * unit.N / unit.mm**2,
        epsilon_cu: 2.28 / 1000,
        epsilon_su: 111.7 / 1000,
    }

    params_zustandslinien = {
        b_auflager: 100 * unit.mm,  # Auflagerbreite
        a_1: 0.11 * unit.m,  # abstand zu A von 0
        a_2: 0.64 * unit.m,  # abstand von A zu C
        a_3: 0.92 * unit.m,  # abstand von C zu B
        a_4: 0.95 * unit.m,  # abstand von B zu D
        b: 800.0 * unit.mm,  # Breite des Trägers
        h: 200.0 * unit.mm,  # Höhe des Trägers,
    }

    Laststufen = np.linspace(1, 320 * 10**3, 100)

    return params_krummung, params_zustandslinien, Laststufen
