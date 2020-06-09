import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.optimize import curve_fit
import cmath

mpl.use('pgf')
mpl.rcParams.update({
'font.family': 'serif',
'text.usetex': True,
'pgf.rcfonts': False,
'pgf.texsystem': 'lualatex',
'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}',
})

# y-Achse ist µA und x-Achse mm
I2 = np.genfromtxt('../data/Messdaten_V406_2.txt', comments='#', unpack=True)
I2[1] = I2[1]
lam = 633*10**-6
_d = 626.1
_b = 0.075        # Spaltbreite
Id = 0.7         # Dunkelstrom


def forReal(x, x0, a, b, c):
    x_ = abs(x - x0)
    d_ = np.sqrt(_d**2 + x_**2)
    sin_phi = x_ / d_
    eta = (np.pi * b * sin_phi) / lam
    return ((a*b*np.sinc(eta))**2 + c)*10**6

# die vorgegebenen Startwere p0 sind wichtig, da der Fit ansonsten total daneben ist. x0 kannten wir ja schon in etwa. Den Dunkelstrom und die Spaltbreite auch
params, cov = curve_fit(forReal, I2[0], I2[1], p0=[12, 1, _b, Id])

x1 = np.linspace(0, I2[0][-1], 200)
plt.plot(I2[0], I2[1], 'b.')
plt.plot(x1, forReal(x1, *params), 'g')
plt.xlabel(r'x \:/\: mm')
plt.ylabel(r'I \:/\: µA')
plt.legend(['Messwerte', 'Ausgleichskurve'])

uncertainties = np.sqrt(np.diag(cov))

for name, value, uncertainty in zip('xabI', params, uncertainties): 
    print(f'{name} = {value:8.8f} ± {uncertainty:.8f}')

plt.savefig('EinzelspaltFit.pdf')