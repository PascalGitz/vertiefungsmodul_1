

import sympy as sp
from sympy.abc import *


# SYMPY SYMBOLE


# Symbole für Zustandslinien Biegeträger

EI, x, F_A, F_B, F_C,  f_B, f_A, f_C = sp.symbols('EI x F_A F_B F_C  f_B, f_A, f_C')
c_1, c_2, c_3,c_4 = sp.symbols('c_1:5', real=True)
a_1, a_2, a_3, a_4 = sp.symbols('a_1:5', positive=True)
b_auflager, l_tot = sp.symbols('b_Auflager l_tot', positive=True)
q_x = sp.Function('q')(x)
M_x = sp.Function('M')(x)
V_x = sp.Function('V')(x)
w_x = sp.Function('w')(x)
phi_x = sp.Function('varphi')(x)
w_1_gerissen_norm = sp.symbols('w_1_II\,SIA')

### Analogieträger Mohr
q_x_a = sp.Function('q_a')(x)
M_x_a = sp.Function('M_a')(x)
V_x_a = sp.Function('V_a')(x)
w_x_a = sp.Function('w_a')(x)
phi_x_a = sp.Function('varphi_a')(x)  


# Symbole für Integration der Krümmung
f_ct, E_c, b, h, W_c, M_r, E_s, f_cc, f_c, f_s550= sp.symbols('f_ct, E_c, b, h, W_c, M_r E_s f_cc f_c f_s550')
A_i, A_c, A_s, s_x, diam_s = sp.symbols('A_i, A_c, A_s, s_x \\oslash_s')
chi_r, I_1 = sp.symbols('chi_r, I^I')
zeta_c, c_nom, I_2 = sp.symbols('zeta_c c_nom I^{II}')
chi_M = sp.Function('chi')(M)
sigma_c_inf_1, F_c1, z_1 = sp.symbols('sigma_c_inf\,1, F_c\,1 z_1')
z_2 = sp.symbols('F_c\,2 z_2')
F_z2, F_c2, f_sy, x_2, epsilon_s2, epsilon_c2, sigma_s2, chi_II, sigma_c_inf_2, M_2 = sp.symbols('F_z\,2 F_c\,2 f_sy x_2 varepsilon_s\,2 varepsilon_c\,2 sigma_s\,2 \chi^{II} sigma_c_inf\,2 M_2')
EI_II, EI_I = sp.symbols('EI^{II} EI^I')
epsilon_sy, x_3, F_c3, F_s3, chi_y, M_y, sigma_c_inf_3 = sp.symbols('varepsilon_sy x_3 F_c\,3, F_s\,3, \chi_y M_y sigma_c_inf\,3')
x_4, M_R, epsilon_cu, epsilon_s4,epsilon_su, chi_u = sp.symbols('x_4 M_R varepsilon_cu varepsilon_s\,4 varepsilon_su chi_u')
EI_III = sp.symbols('EI^{III}')
w_1 = sp.symbols('w_1')
f_su = sp.symbols('f_su')

epsilon_s, epsilon_c = sp.symbols('varepsilon_s varepsilon_c')
sigma_epsilon_s = sp.Function('sigma_s')(epsilon_s)
sigma_epsilon_c = sp.Function('sigma_c')(epsilon_c)



# Symbole für Zugversteifung
lamb, rho_eff, s_rm, w_r, sigma_sr, sigma_sr0 = sp.symbols('lambda rho_eff s_rm w_r sigma_sr sigma_sr0')
delta_chi = sp.Function('\Delta\\chi')(lamb)

substitution_dict = {}

Eq_list = []








