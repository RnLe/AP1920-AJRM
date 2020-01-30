import numpy as np
from scipy.optimize import curve_fit
import math
import matplotlib.pyplot as plt

import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
mpl.rcParams.update({
'font.family': 'serif',
'text.usetex': True,
'pgf.rcfonts': False,
'pgf.texsystem': 'lualatex',
'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}',
})
prefix = '../' if 'python' not in __file__ else ''
data = np.genfromtxt(prefix + 'data/Messdaten_b_und_c.txt', comments='#')
amplituden = []
frequenz = []
phase = []

for i in range(len(data)-1):
    frequenz.append(data[i][0])
    amplituden.append(data[i][1]/2.7)
    phase.append(data[i][4]*np.pi)

x = np.linspace(frequenz[0], frequenz[-1], 200)

def ausgl(x, a, b, c, d):
    return a * (np.log(x*b)/np.log(c)) + d

def anlei(x, a):
    return np.arctan(a*x)

params, cov = curve_fit(anlei, frequenz, phase) # bounds=([-np.inf, 1, 1, -np.inf], np.inf)
errors = np.sqrt(np.diag(cov))

plt.plot(frequenz, phase, '.')
plt.plot(x, anlei(x, *params))
plt.xlabel(r'$f / \mathrm{Hz}$')
plt.ylabel(r'$\varphi(f)$')
plt.legend(['Messwerte', 'Ausgleichskurve'])

plt.savefig(prefix + 'plots/plot_c.pdf')
# print(f'RC = {params[0]:.5f} ± {errors:.5f}')
print('RC = ')
print(params[0])
print(errors)