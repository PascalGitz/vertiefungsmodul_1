import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.integrate import cumtrapz
from scipy.interpolate import interp1d
import astropy.units as un



class Schnittkraefte:
    def __init__(self, path, n, sheetname) -> None:
        # Pfad
        self.path = path
        
        # Rohdaten
        self.df = pd.read_excel(path, sheet_name=sheetname, header=1).fillna(0).drop(index=0)
        # Einheiten hinzufügen
        self.df['Distanz'] = self.df['Distanz']
        self.df['My'] = self.df['My'] 
        self.df['Nx'] = self.df['Nx'] 
        self.df['Vz'] = self.df['Vz'] 
        
        # Stabachse
        self.x = np.linspace(min(self.df['Distanz']), max(self.df['Distanz']), n)*un.meter
        
        # Spacer
        self.n = n
        
        # Schnittkräfte linear auf n interpoliert
        self.My = np.interp(self.x.value, np.array(self.df['Distanz'], dtype=float), np.array(self.df['My'], dtype=float))*un.kilonewton*un.meter
        self.Nx = np.interp(self.x.value, np.array(self.df['Distanz'], dtype=float), np.array(self.df['Nx'], dtype=float))*un.kilonewton
        self.Vz = np.interp(self.x.value, np.array(self.df['Distanz'], dtype=float), np.array(self.df['Vz'], dtype=float))*un.kilonewton


        pass
    
    
class MomentenKruemmung:
    def __init__(self, path, n) -> None:
        # Pfad
        self.path = path
        
        # Rohdaten
        self.df = pd.read_excel(path, sheet_name='momentenkruemmung', header=1).fillna(0).drop(index=0)
        
        # spacer
        self.n = n
        
        # Krümmung und Moment auf n interpoliert
        self.chi_y = np.linspace(min(self.df['cy']), max(self.df['cy']), n)/un.kilometer
        self.My = np.interp(self.chi_y.value, np.array(self.df['cy'], dtype=float), np.array(self.df['My'], dtype=float))*un.kilonewton*un.meter
        pass
    
    def kruemmungsverlauf(self, My):
        # Interpolation der Krümmungswerte
        interpolierte_krümmung = interp1d(self.My.to(un.kilonewton*un.meter), self.chi_y.to(1/un.meter), kind='linear')

        # Berechnung der Krümmung für das gesuchte Biegemoment
        gesuchte_krümmung = interpolierte_krümmung(My.to(un.kilonewton*un.meter))*1/un.meter

        return gesuchte_krümmung
    

if __name__ == '__main__':
    
    ## Sets the path of the script to its location
    os.chdir('C:/Users/Pascal Gitz/OneDrive - Hochschule Luzern/02_Master/03_Tragverhalten_von_Stahlbetontragwerken/docs/src/models/')

    ## reads the data from the FEM model
    path_fem = 'data/Cubus_Versuch_Tue14.xlsx'
    
    
    maximallast = Schnittkraefte(path_fem, 1000, 'Schnittkraefte')
    fiktiv = Schnittkraefte(path_fem, 1000, 'fiktiv_mitte')
    qs1 = MomentenKruemmung(path_fem, 1000)

    print(maximallast.My)








