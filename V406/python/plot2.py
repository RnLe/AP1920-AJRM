import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
#import scipy.constants as const

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

U,Z,DZ,N,DN = np.genfromtxt("../data/strom.csv",delimiter=",",unpack=True)

plt.errorbar(U, Z, yerr=DZ, fmt='rx', label='Freigesetzte Ladung')
plt.xlabel(r'$U\,/\,\si{\volt}$')
plt.ylabel(r'$Z\,/\,\num{e9}$')
plt.grid()
plt.legend()
plt.savefig("../plots/strom1.pdf")

#plt.clf()
#
#plt.errorbar(N, Z, xerr=DN, yerr=DZ, fmt='rx', label='Freigesetzte Ladung')
#plt.xlabel(r'$N\,/\,\si{\second\tothe{-1}}$')
#plt.ylabel(r'$Z\,/\,\num{e9}\symup{e}$')
#plt.grid()
#plt.legend()
#plt.savefig("../plots/strom2.pdf")