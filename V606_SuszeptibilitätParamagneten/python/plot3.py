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

U,Z,DZ,N,DN = np.genfromtxt("../data/strom.csv",delimiter=",",unpack=True)

#U,NI = np.genfromtxt("../data/kennlinie.csv",delimiter=",",unpack=True)
#N=NI/60 #Impulsrate
#deltaN=np.sqrt(N)

plt.errorbar(U, Z, yerr=DZ, fmt='x',color='teal', label='Messwerte')
#plt.axvline(660,color='C5',label=r'Plateau-Bereich')
#plt.axvline(360,color='C5')
plt.xlabel(r'$U\,/\,\si{\volt}$')
plt.ylabel(r'$Z\,/\,\num{e9}$')

def f1(x,m,b):
    return m*x+b

# Fit
params, cov = curve_fit(f1, U, Z, sigma=1./(DZ*DZ))
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

plt.grid()
plt.legend()
plt.savefig("../plots/StromRegr.pdf")


#fit parameter 1-sigma error
#———————————–
#0.13803487721750196 +- 0.006186950589020715
#-38.206853873675115 +- 3.259238990112341