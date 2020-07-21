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

mu=np.array([12.0,12.5,13.0,13.5,14.0,14.5,15.0,15.5,16.0,16.5,17.0,17.5,18.0,18.5,19.0,19.5])
v=np.array([44.6,44.6,54.1,63.6,73.2,85.9,89.1,92.3,85.9,70.0,57.3,47.7,44.6,50.9,60.5,60.5])
I=np.array([19,60,115,170,230,270,300,330,400,450,450,310,200,110,90,100])
R=5 # mm

def velocity(r,vmax):
    return vmax*(1-np.absolute(r)/R)**(1/2)

#plt.xlabel(r'$\mu\,/\,\si{\micro\second}$')
#plt.ylabel(r'$v\,/\,\si{\centi\meter\per\second}$')
#plt.plot(mu, v, 'x', color='maroon', label='Geschwindigkeit')
#plt.legend()
#plt.grid(':')
#plt.savefig('../plots/70velocity.pdf')
#plt.clf()
#
#plt.xlabel(r'$\mu\,/\,\si{\micro\second}$')
#plt.ylabel(r'$I\,/\,\SI{e3}{\volt\squared\per\second}$')
#plt.plot(mu, I, 'x', color='teal', label='Intensität')
#plt.legend()
#plt.grid(':')
#plt.savefig('../plots/70intensity.pdf')
#plt.clf()

abszisse=(mu-15.25)*3/2 # abszisse entspricht variable r in mm
#print(abszisse)
abs_richtig=abszisse[0:14] # nur die Werte for r<R

params, covariance_matrix = curve_fit(velocity, abs_richtig, v[0:14])
uncertainties = np.sqrt(np.diag(covariance_matrix))
for name, value, uncertainty in zip('v', params, uncertainties): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')

nstd=1.
x_plot=np.linspace(-5,5)
params_up = params + nstd * uncertainties
params_dw = params - nstd * uncertainties
fit =    velocity(x_plot, *params)
fit_up1 = velocity(x_plot, *params_up)
fit_dw1 = velocity(x_plot, *params_dw)
nstd=2.
params_up = params + nstd * uncertainties
params_dw = params - nstd * uncertainties
fit =    velocity(x_plot, *params)
fit_up2 = velocity(x_plot, *params_up)
fit_dw2 = velocity(x_plot, *params_dw)
nstd=3.
params_up = params + nstd * uncertainties
params_dw = params - nstd * uncertainties
fit =    velocity(x_plot, *params)
fit_up3 = velocity(x_plot, *params_up)
fit_dw3 = velocity(x_plot, *params_dw)

plt.plot(x_plot, velocity(x_plot, *params), "-",color='green',label=r'Näherungsfunktion')
plt.fill_between(x_plot, fit_up1, fit_dw1, color='forestgreen', alpha=.25, label=r'$1\sigma$-Intervall')
plt.fill_between(x_plot, fit_up2, fit_up1, color='limegreen', alpha=.25, label=r'$2\sigma$-Intervall')
plt.fill_between(x_plot, fit_dw1, fit_dw2, color='limegreen', alpha=.25)
plt.fill_between(x_plot, fit_up3, fit_up2, color='lightgreen', alpha=.25, label=r'$3\sigma$-Intervall')
plt.fill_between(x_plot, fit_dw2, fit_dw3, color='lightgreen', alpha=.25)
plt.plot(abs_richtig,v[0:14],"x",color='maroon',label='Messwerte')
plt.ylabel(r'$v\,/\,\si{\centi\meter\per\second}$')
plt.xlabel(r'$r\,/\,\si{\milli\meter}$')
plt.legend()
plt.grid(':')
plt.savefig('../plots/70regr.pdf')
plt.clf()

v=np.array([47.7,27.0,27.0,31.8,35.0,38.2,41.4,41.4,38.2,31.8,28.6,25.5,25.5,28.6,30.0,30.0])
I=np.array([  7, 30, 80,100,170,230,250,280,300,330,300,200,100, 50, 50, 60])

#plt.xlabel(r'$\mu\,/\,\si{\micro\second}$')
#plt.ylabel(r'$v\,/\,\si{\centi\meter\per\second}$')
#plt.plot(mu, v, 'x', color='maroon', label='Geschwindigkeit')
#plt.legend()
#plt.grid(':')
#plt.savefig('../plots/45velocity.pdf')
#plt.clf()

#plt.xlabel(r'$\mu\,/\,\si{\micro\second}$')
#plt.ylabel(r'$I\,/\,\SI{e3}{\volt\squared\per\second}$')
#plt.plot(mu, I, 'x', color='teal', label='Intensität')
#plt.legend()
#plt.grid(':')
#plt.savefig('../plots/45intensity.pdf')

#params, covariance_matrix = curve_fit(velocity, abs_richtig, v[0:14])
#uncertainties = np.sqrt(np.diag(covariance_matrix))
#for name, value, uncertainty in zip('v', params, uncertainties): 
#    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')
#
#nstd=1.
#x_plot=np.linspace(-5,5)
#params_up = params + nstd * uncertainties
#params_dw = params - nstd * uncertainties
#fit =    velocity(x_plot, *params)
#fit_up1 = velocity(x_plot, *params_up)
#fit_dw1 = velocity(x_plot, *params_dw)
#nstd=2.
#params_up = params + nstd * uncertainties
#params_dw = params - nstd * uncertainties
#fit =    velocity(x_plot, *params)
#fit_up2 = velocity(x_plot, *params_up)
#fit_dw2 = velocity(x_plot, *params_dw)
#nstd=3.
#params_up = params + nstd * uncertainties
#params_dw = params - nstd * uncertainties
#fit =    velocity(x_plot, *params)
#fit_up3 = velocity(x_plot, *params_up)
#fit_dw3 = velocity(x_plot, *params_dw)
#
#plt.plot(x_plot, velocity(x_plot, *params), "-",color='green',label=r'Näherungsfunktion')
#plt.fill_between(x_plot, fit_up1, fit_dw1, color='forestgreen', alpha=.25, label=r'$1\sigma$-Intervall')
#plt.fill_between(x_plot, fit_up2, fit_up1, color='limegreen', alpha=.25, label=r'$2\sigma$-Intervall')
#plt.fill_between(x_plot, fit_dw1, fit_dw2, color='limegreen', alpha=.25)
#plt.fill_between(x_plot, fit_up3, fit_up2, color='lightgreen', alpha=.25, label=r'$3\sigma$-Intervall')
#plt.fill_between(x_plot, fit_dw2, fit_dw3, color='lightgreen', alpha=.25)
#plt.plot(abs_richtig,v[0:14],"x",color='maroon',label='Messwerte')
#plt.ylabel(r'$v\,/\,\si{\centi\meter\per\second}$')
#plt.xlabel(r'$r\,/\,\si{\milli\meter}$')
#plt.legend()
#plt.grid(':')
#plt.savefig('../plots/45regr.pdf')
#