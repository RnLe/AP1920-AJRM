import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

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

a2=np.array([50.5,98.5,162.5,242.5,338.5,450.5,578.5,722.5,882.5,1058.5]) #in cm^2
T2=np.array([6.25,8.58,10.30,14.67,17.31,22.09,27.77,33.52,39.31,45.97]) #in s^2

#plt.plot(a2, T2, 'd', label="Messwerte")

# Lineare Regression
params, covariance_matrix = np.polyfit(a2*10**(-4), T2, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('cb', params, errors): #c steigung, b achsenabschnitt
    print(f'{name} = {value:.3f} ± {error:.3f}')

#x_plot = np.linspace(50, 1100)
#
#plt.plot(
#    x_plot,
#    params[0] * x_plot *10**(-4) + params[1],
#    label='Lineare Regression',
#    linewidth=3,
#)
#plt.legend(loc="best")
#
#plt.xlabel(r'$a^2 \:/\: \si{\centi\meter\squared}$')
#plt.ylabel(r'$T^2 \:/\: \si{\second\squared}$')
#
#plt.savefig("plot_I_D.pdf")