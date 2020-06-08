import numpy as np
import matplotlib.pyplot as plt
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

t = np.genfromtxt("data/A_times.csv",delimiter=",",unpack=True,usecols=0) #sind in 10^-3 s abgespeichert
U_C = np.genfromtxt("data/A_lnU_C.csv",delimiter=",",unpack=True,usecols=0)

lnUNull=np.log(4.8) #ln(4.8)

plt.plot(t,U_C,'g*',label="Messwerte")
plt.yscale('log') #logarithmische y-Achse
plt.grid()
plt.legend()
plt.xlabel(r'$t / 10^{-3} \, \mathrm{s}$')
plt.ylabel(r'$U_C \,/\, \mathrm{V}$')
plt.savefig("plots/plot_messw.pdf")

plt.clf()

params, covariance_matrix = np.polyfit(t*10**(-3), np.log(U_C), deg=1, cov=True) # mit einer linearen Funktion fitten

errors = np.sqrt(np.diag(covariance_matrix)) #Fehler=wurzel der kovarianzmatrix

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}') # Ausgabe: a und b mit y=a*x + b

plt.plot(t,U_C,'r*',label="Messwerte")
x_plot = np.linspace(-2.5, -0.25)
plt.plot(x_plot,np.exp(params[0]*x_plot*10**(-3)+params[1]),label="Lineare Regression")
plt.legend(loc="best")
plt.grid()
plt.yscale('log') #logarithmische y-Achse
plt.xlabel(r'$t / 10^{-3} \mathrm{s}$')
plt.ylabel(r'$U_C \,/\, \mathrm{V}$')
plt.savefig("plots/ausgleichsgerade.pdf")

# Ausgabe: 
# a = -1221.631 ± 18.673
# b = -1.561 ± 0.029

# Konstante B (vgl. auswertung.text/main.pdf) berechnen mit Unsicherheiten
# B=RC(b - ln U_0)=-1/a (b - ln U_0)
a=ufloat(params[0],errors[0]) 
b=ufloat(params[1],errors[1])
B=(-1/a)*(b-lnUNull)
print('B ist ',B.n,'plusminus',B.s)

#Ausgabe: B ist  -0.0025620930329117494 plusminus 4.59548003834578e-05