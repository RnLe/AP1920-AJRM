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

# y-Achse ist µA und x-Achse mm
# -> daher alle Werte in mm und µA umrechnen
I2 = np.genfromtxt('../data/Messdaten_V406_2.txt', comments='#', unpack=True)
lam = 633*10**-6    # Wellenlänge
_d = 626.1          # Abstand zum Sensor
_b = 0.075          # Spaltbreite
Id = 0.81           # Dunkelstrom
x_0 = 11.727

def forReal(x, x0, a, b, c):
    x_ = abs(x - x0)
    d_ = np.sqrt(_d**2 + x_**2)
    sin_phi = x_ / d_
    eta = (np.pi * b * sin_phi) / lam
    return ((a*np.sinc(eta/np.pi))**2)*10**6 + c

params, cov = curve_fit(forReal, I2[0], I2[1], p0=[x_0, 0.001, _b, Id], bounds=(0, 15))

# def forReal(x, a):
#     x_ = abs(x - x_0)
#     d_ = np.sqrt(_d**2 + x_**2)
#     sin_phi = x_ / d_
#     eta = (np.pi * _b * sin_phi) / lam
#     return ((a*np.sinc(eta/np.pi))**2)*10**6 + Id

# params, cov = curve_fit(forReal, I2[0], I2[1], p0=[0.001], bounds=(0, 15))

uncertainties = np.sqrt(np.diag(cov))

for name, value, uncertainty in zip('xabI', params, uncertainties): 
    print(f'{name} = {value:8.8f} ± {uncertainty:.8f}')

if plot:
    x1 = np.linspace(0, I2[0][-1], 200)
    plt.tight_layout()
    plt.plot(I2[0], I2[1], 'b.')
    plt.plot(x1, forReal(x1, *params), 'g')
    plt.xlabel(r'x \:/\: mm')
    plt.ylabel(r'I \:/\: µA')
    plt.legend(['Messwerte', 'Ausgleichskurve'])


    plt.savefig('EinzelspaltFits.pdf')