import numpy as np
import scipy.optimize as so
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties.unumpy import nominal_values as noms
import matplotlib.pyplot as plt

r, U, PA, LI, LP = np.genfromtxt('LED.txt', unpack=True)
U /= LI*LP*PA   #faktoren auf U anwenden
r *= 10**-2     #cm in m
def f(r, a, b, c):
    return a + b / (r + c)**2

parameters, pcov = so.curve_fit(f, r, U)
param2 = np.array([0, 5, -6])       #so sind die Parameter definiert, welche von so.curve zurückgegeben werden
x = np.linspace(r[0], r[-1], 1000)      #ein x definieren, welches gleichmäßg über den Wertebereich von r läuft



def ucurve_fit(f, x, y, **kwargs):
    if np.any(unp.std_devs(y) == 0):
        sigma = None
    else:
        sigma = unp.std_devs(y)

    popt, pcov = so.curve_fit(f, x, unp.nominal_values(y), sigma=sigma, **kwargs)

    return unc.correlated_values(popt, pcov)

A, B, C = ucurve_fit(f, r, U)
plt.plot(r, U, 'y+', label='Original')
plt.plot(x, f(x, *parameters), 'b', label='Fit')
plt.plot(x, noms(f(x, A, B, C)), 'r', label='uFit')
plt.show()