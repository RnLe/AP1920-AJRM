import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
#import scipy.constants as const
from pylab import *
from scipy.optimize import curve_fit

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

data = np.genfromtxt("../data/Vanadium.dat", unpack=True, comments='#')

data_minus_null = data[1]-14

# i = 1
# for x in data[1]:
#     print(int(x))
#     if (i == 22): print('')
#     i += 1

# i = 1
# for x in np.sqrt(data[1]):
#     print(int(x))
#     if (i == 22): print('')
#     i += 1

y_err = np.sqrt(data_minus_null)

plt.errorbar(data[0], data_minus_null, y_err, marker='x', fmt='x', label='Messwerte ohne Untergrund')
plt.yscale('log')
plt.xlabel(r'$t\,/\,\si{\second}$')
plt.ylabel(r'$N_\text{V}$')
plt.grid('.')

# plt.savefig("../plots/Vanadium.pdf")

N_0 = data[1][0]    # Anzahl instabiler Kerne zu Beginn der Messung
delta_t = 30
def y(x, a, b):
    return a*x + b

p = np.polyfit(data[0], np.log(data_minus_null), 1)
params, cov = curve_fit(y, data[0], np.log(data_minus_null), p0=p, sigma=1./((np.log(y_err))**2))
err = np.sqrt(np.diag(cov))

x = np.linspace(data[0][0], data[0][-1], 200)
plt.plot(x, np.exp(y(x, *params)), label='Ausgleichsgerade')

nstd = 1. # to draw 1-sigma intervals
params_up = params + nstd * err
params_dw = params - nstd * err

fit =    y(data[0], *params)
fit_up = y(data[0], *params_up)
fit_dw = y(data[0], *params_dw)

plt.fill_between(data[0], np.exp(fit_up), np.exp(fit_dw), color='lightseagreen', alpha=.25, label=r'$1\sigma$-Intervall')

plt.legend()
plt.savefig("../plots/Vanadium_AusgleichSigma.pdf")
plt.close()

p = np.polyfit(data[0][:21], np.log(data_minus_null[:21]), 1)
params, cov = curve_fit(y, data[0][:21], np.log(data_minus_null[:21]), p0=p)
err = np.sqrt(np.diag(cov))

plt.errorbar(data[0][:21], data_minus_null[:21], y_err[:21], marker='x', fmt='x', label='Messwerte ohne Untergrund')
plt.yscale('log')
plt.xlabel(r'$t\,/\,\si{\second}$')
plt.ylabel(r'$N_\text{V}$')
plt.grid('.')
plt.plot(x, np.exp(y(x, *params)), label='Ausgleichsgerade 2')
plt.legend()
# plt.savefig("../plots/Vanadium_Ausgleich_2.pdf")

print(params)
print(err)