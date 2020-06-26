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

t,N=np.genfromtxt("../data/Rhodium.csv",delimiter=',',unpack=True)
N_Rh=N-7
DeltaN_Rh=np.sqrt(N_Rh)
print("Rhodium: Anzahl ohne Untergrund: ",N_Rh,",\tFehler: ",DeltaN_Rh)

plt.errorbar(t,N_Rh,xerr=7.5,yerr=DeltaN_Rh,fmt='x',label='Messwerte ohne Untergrund')
plt.yscale('log')
plt.xlabel(r'$t\,/\,\si{\second}$')
plt.ylabel(r'$N_\text{Rh}$')
plt.grid('.')
plt.legend()
plt.savefig("../plots/Rhodium.pdf")

plt.clf()
#t_Sternchen=330
#Berechnung des langsamen Zerfalls
y_langsam=np.log(N_Rh[21:])
deltay_langsam=np.log(DeltaN_Rh[21:])
x_langsam=t[21:]

def linearGerade(x,m,b):
    return m*x+b

params, cov = curve_fit(linearGerade, x_langsam, y_langsam, sigma=1./(deltay_langsam*deltay_langsam))
err = np.sqrt(np.diag(cov))

print('fit parameter 1-sigma error')
print('———————————–')
for i in range(len(params)):
    print(str(params[i])+' +- '+str(err[i])) #str() gibt den zugehörigen String zurück
#err gibt einen Fehler von ein sigma zurück

nstd = 1. # to draw 1-sigma intervals
params_up = params + nstd * err
params_dw = params - nstd * err

fit =    linearGerade(t, *params)
fit_up = linearGerade(t, *params_up)
fit_dw = linearGerade(t, *params_dw)

plt.errorbar(t[21:],N_Rh[21:],xerr=7.5,yerr=DeltaN_Rh[21:],fmt='x',label='langsamer Zerfall',color='teal')
plt.errorbar(t[:21],N_Rh[:21],xerr=7.5,yerr=DeltaN_Rh[:21],fmt='x',label='schneller Zerfall',color='darkgray')
plt.yscale('log')
plt.xlabel(r'$t\,/\,\si{\second}$')
plt.ylabel(r'$N_\text{Rh}$')
plt.grid('.')
plt.plot(t, np.exp(fit), color='darkslategray', label='Lineare Approximation')
plt.fill_between(t, np.exp(fit_up), np.exp(fit_dw), color='lightseagreen', alpha=.25, label=r'$1\sigma$-Intervall')

plt.legend()
plt.savefig("../plots/Rhodium_langsam.pdf")

plt.clf()
#schneller Zerfall

def langsam(x): #gibt ln(N_langsam) zurück
    return linearGerade(x, *params)

x_schnell=t[:16] #alles bis inklusive 240 Sekunden
y_kombi=np.log(N_Rh[:16])
deltay_schnell=np.log(DeltaN_Rh[:16])
# Fehler m+ssen ja gleich bleiben, da ändert sich nix
y_schnell=np.log(np.exp(y_kombi)-np.exp(langsam(x_schnell)))

params2, cov2 = curve_fit(linearGerade, x_schnell, y_schnell, sigma=1./(deltay_schnell*deltay_schnell))
err2 = np.sqrt(np.diag(cov2))

print('fit parameter 1-sigma error')
print('———————————–')
for i in range(len(params2)):
    print(str(params2[i])+' +- '+str(err2[i])) #str() gibt den zugehörigen String zurück
#err gibt einen Fehler von ein sigma zurück

nstd = 1. # to draw 1-sigma intervals
params_up2 = params2 + nstd * err2
params_dw2 = params2 - nstd * err2

fit2 =    linearGerade(t[:16], *params2)
fit_up2 = linearGerade(t[:16], *params_up2)
fit_dw2 = linearGerade(t[:16], *params_dw2)

#plt.errorbar(t[16:],N_Rh[16:],xerr=7.5,yerr=DeltaN_Rh[16:],fmt='x',label='langsamer Zerfall',color='darkgray')
plt.errorbar(t[:16],np.exp(y_schnell)[:16],xerr=7.5,yerr=DeltaN_Rh[:16],fmt='x',label='schneller Zerfall',color='teal')
plt.yscale('log')
plt.xlabel(r'$t\,/\,\si{\second}$')
plt.ylabel(r'$N_\text{Rh}$')
plt.grid('.')
plt.plot(t[:16], np.exp(fit2), color='darkslategray', label='Lineare Approximation')
plt.fill_between(t[:16], np.exp(fit_up2), np.exp(fit_dw2), color='lightseagreen', alpha=.25, label=r'$1\sigma$-Intervall')

plt.legend()
plt.savefig("../plots/Rhodium_schnell.pdf")

plt.clf()

#Letzter Plot

fit3   =linearGerade(t,*params2)
fit_up3=linearGerade(t,*params_up2)
fit_dw3=linearGerade(t,*params_dw2)

plt.errorbar(t,N_Rh,xerr=7.5,yerr=DeltaN_Rh,fmt='x',label='Messwerte',color='teal')
#plt.errorbar(t[:21],N_Rh[:21],xerr=7.5,yerr=DeltaN_Rh[:21],fmt='x',label='schneller Zerfall',color='darkgray')
plt.yscale('log')
plt.xlabel(r'$t\,/\,\si{\second}$')
plt.ylabel(r'$N_\text{Rh}$')
plt.grid('.')
plt.plot(t, np.exp(fit)+np.exp(fit3), color='darkslategray', label='Lineare Approximation')
plt.fill_between(t, np.exp(fit_up)+np.exp(fit_up3), np.exp(fit_dw)+np.exp(fit_dw3), color='lightseagreen', alpha=.25, label=r'$1\sigma$-Intervall')

plt.legend()

plt.savefig('Rhodium_kombi.pdf')