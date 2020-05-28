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


U,NI = np.genfromtxt("../data/kennlinie.csv",delimiter=",",unpack=True)
N=NI/60 #Impulsrate
deltaN=np.sqrt(N)

#plt.errorbar(U, N, yerr=deltaN, fmt='rx', label='Messwerte')
plt.errorbar(U[4:35], N[4:35], yerr=deltaN[4:35],color='teal',fmt='x', label='Plateau-Bereich')
plt.errorbar(U[:4], N[:4], yerr=deltaN[:4],fmt='x', color='darkgray', label='außerhalb des Plateaus')
plt.errorbar(U[35:], N[35:], yerr=deltaN[35:],fmt='x', color='darkgray')

#plt.axvline(660,color='C5',label=r'Plateau-Bereich')
#plt.axvline(360,color='C5')
plt.xlabel(r'$U\,/\,\si{\volt}$')
plt.ylabel(r'$N\,/\,\si{\per\second}$')
plt.grid()
plt.legend()
plt.savefig("../plots/plateau.pdf")

plt.clf()

def f1(x,m,b):
    return m*x+b

#plt.errorbar(U, N, yerr=deltaN, fmt='rx', label='Messwerte')
#plt.axvline(660,color='C5',label=r'Plateau-Bereich')
#plt.axvline(360,color='C5')
plt.errorbar(U[4:35], N[4:35], yerr=deltaN[4:35],fmt='x',color='teal', label='Plateau-Bereich')
plt.errorbar(U[:4], N[:4], yerr=deltaN[:4],fmt='x', color='darkgray', label='außerhalb des Plateaus')
plt.errorbar(U[35:], N[35:], yerr=deltaN[35:],fmt='x', color='darkgray')
plt.xlabel(r'$U\,/\,\si{\volt}$')
plt.ylabel(r'$N\,/\,\si{\per\second}$')
plt.grid()

# Fit
params, cov = curve_fit(f1, U[4:35], N[4:35], sigma=1./(deltaN[4:35]*deltaN[4:35]))
err = np.sqrt(np.diag(cov))

print('fit parameter 1-sigma error')
print('———————————–')
for i in range(len(params)):
    print(str(params[i])+' +- '+str(err[i])) #str() gibt den zugehörigen String zurück
#err gibt einen Fehler von ein sigma zurück

nstd = 1. # to draw 1-sigma intervals
params_up = params + nstd * err
params_dw = params - nstd * err

fit = f1(U, *params)
fit_up = f1(U, *params_up)
fit_dw = f1(U, *params_dw)

plt.plot(U, fit, color='darkslategray', label='Lineare Approximation')
plt.fill_between(U, fit_up, fit_dw,color='lightseagreen', alpha=.25, label=r'Fehler-Intervall')

plt.legend()
plt.savefig("../plots/plateau_err.pdf")

#fit parameter 1-sigma error
#———————————–
#0.02304381096115296 +- 0.0032885015034107745
#157.8974444189741 +- 1.7097397013435573