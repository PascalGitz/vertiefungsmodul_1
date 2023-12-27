import numpy as np
import matplotlib.pyplot as plt
from sectionproperties.pre.library import circular_section, rectangular_section

import concreteproperties.stress_strain_profile as ssp
from concreteproperties import (
    Concrete,
    ConcreteSection,
    SteelBar,
    add_bar_rectangular_array,
)
from concreteproperties.results import MomentCurvatureResults


### MATERIAL

#### beton


conc_nonlinear = Concrete(
    name="Beton nicht-linear",
    density=2.4e-6,
    stress_strain_profile=ssp.EurocodeNonLinear(
        elastic_modulus=38e3,
        ultimate_strain=0.003,
        compressive_strength=35,
        compressive_strain=0.0035,
        tensile_strength=3.5,
        tension_softening_stiffness=10e3,
    ),
    ultimate_stress_strain_profile=ssp.BilinearStressStrain(
        compressive_strength=35,
        compressive_strain=0.0030,
        ultimate_strain=0.0035,
    ),
    flexural_tensile_strength=3.5,
    colour="lightgrey",
)


#### Hochfester Stahl
SAS670 = SteelBar(
    name="SAS 670 - Bilineares Verhalten",
    density=7.85e-6,
    stress_strain_profile=ssp.SteelHardening(
        yield_strength=670,
        elastic_modulus=200e3,
        fracture_strain=50/1000,
        ultimate_strength=800,
    ),
    colour="darkblue",
)

#### baustahl
Bst550 = SteelBar(
    name="Bst 550 - Bilineares Verhalten",
    density=7.85e-6,
    stress_strain_profile=ssp.SteelHardening(
        yield_strength=550,
        elastic_modulus=200e3,
        fracture_strain=50/1000,
        ultimate_strength=594,
    ),
    colour="lightblue",
)






### GEOMETRIE

col = rectangular_section(d=450, b=170)

# add bars to column
qs_druckbewehrung = add_bar_rectangular_array(
    geometry=col,
    area=10**2/4*np.pi,
    material=Bst550,
    n_x=2,
    x_s=170/2,
    n_y=1,
    y_s=0,
    anchor=((170-170/2)/2, 420),
    exterior_only=True,
)

qs_zugbewehrung = add_bar_rectangular_array(
    geometry=qs_druckbewehrung,
    area=18**2/4*np.pi,
    material=SAS670,
    n_x=2,
    x_s=170/2,
    n_y=1,
    y_s=0,
    anchor=((170-170/2)/2, 30),
    exterior_only=True,
)

querschnitt = add_bar_rectangular_array(
    geometry=qs_zugbewehrung,
    area=12**2/4*np.pi,
    material=Bst550,
    n_x=1,
    x_s=170/2,
    n_y=1,
    y_s=0,
    anchor=(170/2, 25),
    exterior_only=True,
)




querschnitt.geoms[0].material = conc_nonlinear

conc_querschnitt = ConcreteSection(querschnitt)

moment_kruemmung_nonlin = conc_querschnitt.moment_curvature_analysis(
    theta=0, kappa_inc=2.5e-7, progress_bar=False
)



def kruemmungsverlauf(My_start, chi_y, My):
    # Interpolation der Krümmungswerte
    interpolierte_krümmung = interp1d(My_start, chi_y, kind='linear')

    # Berechnung der Krümmung für das gesuchte Biegemoment
    gesuchte_krümmung = interpolierte_krümmung(My)

    return gesuchte_krümmung