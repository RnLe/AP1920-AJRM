import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.optimize import curve_fit
import cmath
import sys

mpl.use('pgf')
mpl.rcParams.update({
'font.family': 'serif',
'text.usetex': True,
'pgf.rcfonts': False,
'pgf.texsystem': 'lualatex',
'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}',
})

plot = True if len(sys.argv) != 1 and "-plot" in sys.argv else False
einzel = True if len(sys.argv) != 1 and "-einzel" in sys.argv else False

# y-Achse ist µA und x-Achse mm
# -> daher alle Werte in mm und µA umrechnen
I2 = np.genfromtxt('../data/Messdaten_V406_1.txt', comments='#', unpack=True)
lam = 633*10**-6    # Wellenlänge
_d = 626.1          # Abstand zum Sensor
Id = 0.82           # Dunkelstrom
_s = 0.75           # Spaltabstand
_b = 0.15           # Spaltbreite
x_0 = 11.077


def forImaginary(x, x0, a, b, c, s):
    x_ = abs(x - x0)
    d_ = np.sqrt(_d**2 + x_**2)
    sin_phi = x_ / d_
    eta = (np.pi * sin_phi) / lam
    return ((2*a*np.sinc(eta*b/np.pi)*np.cos(eta*s))**2)*10**6 + c


params, cov = curve_fit(forImaginary, I2[0], I2[1], p0=[x_0, 0.01, _b, Id, 0.01], bounds=(0, 15))

if einzel:
    def forReal(x, x0, a, b, c):
        x_ = abs(x - x0)
        d_ = np.sqrt(_d**2 + x_**2)
        sin_phi = x_ / d_
        eta = (np.pi * b * sin_phi) / lam
        return ((a*np.sinc(eta/np.pi))**2)*10**6 + c


    params, cov = curve_fit(forReal, I2[0], I2[1], p0=[x_0, 0.01, _b, Id], bounds=(0, 15))

uncertainties = np.sqrt(np.diag(cov))

for name, value, uncertainty in zip('xabIs', params, uncertainties): 
    print(f'{name} = {value:8.8f} ± {uncertainty:.8f}')

if plot:
    if not einzel:
        x1 = np.linspace(0, I2[0][-1], 500)
        plt.plot(I2[0], I2[1], 'b.')
        plt.plot(x1, forImaginary(x1, *params), 'g')
        plt.xlabel(r'x \:/\: mm')
        plt.ylabel(r'I \:/\: µA')
        plt.legend(['Messwerte', 'Ausgleichskurve'])


        plt.savefig('DoppelspaltFit.pdf')

        # --------------------------------------- Fit mit Einzelspaltfunktion
        print()
    else:
        plt.close()

        x1 = np.linspace(0, I2[0][-1], 200)
        plt.plot(I2[0], I2[1], 'b.')
        plt.plot(x1, forReal(x1, *params), 'g')
        plt.xlabel(r'x \:/\: mm')
        plt.ylabel(r'I \:/\: µA')
        plt.legend(['Messwerte', 'Ausgleichskurve'])


        plt.savefig('DoppelspaltFitEinzel.pdf')