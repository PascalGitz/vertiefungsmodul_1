# plot_style.py

import matplotlib.pyplot as plt
import numpy as np

def set_engineering_style():
    plt.style.use('ggplot')  # Zurücksetzen auf den Matplotlib-Standardstil
    plt.rcParams['lines.linewidth'] = 1.0  # Linienstärke
    plt.rcParams['axes.grid'] = True  # Gitterlinien im Plot
    plt.rcParams['axes.labelsize'] = 12  # Größe der Achsenbeschriftungen
    plt.rcParams['axes.titlesize'] = 14  # Größe des Plot-Titels
    plt.rcParams['axes.facecolor'] = 'white' # Hintergrund weiß
    plt.rcParams['axes.edgecolor'] = 'black' # Achsen schwarz
    plt.rcParams['axes.linewidth'] = 0.5 # Achsen schwarz
    plt.rcParams['text.color'] = 'black' # Text schwarz
    
    # plt.rcParams['xtick.direction'] = 'in' # Teilstriche innerhalb des Plots
    # plt.rcParams['ytick.direction'] = 'in'

    plt.rcParams['xtick.labelsize'] = 10  # Größe der x-Achsenbeschriftungen
    plt.rcParams['ytick.labelsize'] = 10  # Größe der y-Achsenbeschriftungen
    plt.rcParams['legend.fontsize'] = 10  # Größe der Legende
    plt.rcParams['figure.figsize'] = (5, 2)  # Größe der Figur
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Palatino Linotype"],
        "text.usetex": True,
        "font.size": 12,
    })
    
def plot_example():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y, label='Sinus-Funktion', color='k')
    plt.xlabel('X-Achse')
    plt.ylabel('Y-Achse')
    plt.title('Beispielplot')
    plt.legend()
    plt.show()

