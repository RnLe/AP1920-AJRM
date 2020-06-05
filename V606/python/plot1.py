import matplotlib.pyplot as plt
import numpy as np
#from uncertainties import ufloat
#import scipy.constants as const
#from pylab import *
#from scipy.optimize import curve_fit

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


f,UA = np.genfromtxt("../data/a.csv",delimiter=",",unpack=True)

plt.plot(f,UA,'x',label=r'Filterkurve',color='darkgreen')
plt.axvline(21.5,linestyle=':',color='yellowgreen',label=r'Übergang')
plt.axvline(29.5,linestyle=':',color='yellowgreen')
plt.axvline(33.5,linestyle=':',color='yellowgreen')
plt.axvline(36.5,linestyle=':',color='yellowgreen')
plt.yscale('log')
plt.xlabel(r'$\nu\,/\,\si{\kilo\hertz}$')
plt.ylabel(r'$U_\text{A}\,/\,\si{\milli\volt}$')
#plt.grid()
plt.legend()
plt.savefig("../plots/Filterkurve.pdf")
