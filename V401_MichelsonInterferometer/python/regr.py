import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import scipy.constants as const

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

e=const.physical_constants["elementary charge"]

z=np.array([30,31,35,37,38,40]) #Ordnungszahl
sig=np.array([3.62,3.68,3.84,4.07,4.11,4.33])
E_keV=np.array([9.6154176,10.32185278,13.47951301,15.08974341,16.00232593,17.77862823]) #Energie in keV
E_J=E_keV*e[0]*10**3 #Energie in Joule

params, covariance_matrix = np.polyfit(z-sig, np.sqrt(E_keV), deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))
for name, value, error in zip('mb', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

achse=np.linspace(25.5,36.5)
plt.plot(z-sig,np.sqrt(E_keV),"rx",label="Messwerte")
plt.plot(achse,params[0]*achse+params[1],label="Lineare Regression")
plt.xlabel(r'$z-\sigma _\text{K}$')
plt.ylabel(r'$\sqrt{E_\text{K}\,/\,\SI{e3}{\electronvolt}}$')
plt.legend()
plt.grid()
plt.savefig("../plots/regression2.pdf")