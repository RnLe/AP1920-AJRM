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

U_A,I_A=np.genfromtxt("../data/energie.csv",delimiter=",",unpack=True)

#plt.plot(U_A,I_A,"x",color='indianred',label='Messwerte')
#plt.ylabel(r'$I_\text{A}\,/\,\si{\nano\ampere}$')
#plt.xlabel(r'$U_\text{A}\,/\,\si{\volt}$')
#plt.grid(':')
#plt.legend()
#plt.savefig("../plots/Energie.pdf")
#
#plt.clf()

#plt.plot(U_A,I_A,":",color='indianred',label='Messwerte')
#plt.ylabel(r'$I_\text{A}\,/\,\si{\nano\ampere}$')
#plt.xlabel(r'$U_\text{A}\,/\,\si{\volt}$')
#plt.grid(':')
#plt.legend()
#plt.savefig("../plots/Energie2.pdf")

plt.clf()

a=I_A.size-1
Diff_I=np.zeros(a+1)
for i in range(a):
    Diff_I[i]=I_A[i]-I_A[i+1]

#plt.plot(U_A[:a],Diff_I,"x",color="lightcoral",label="Messwerte")
#plt.ylabel(r'$(I_\text{A}(U)-I_\text{A}(U+\Delta U))\,/\,\si{\nano\ampere}$')
#plt.xlabel(r'$U_\text{A}\,/\,\si{\volt}$')
#plt.grid(':')
#plt.legend()
#plt.savefig("../plots/EnergieDiff.pdf")
#
#plt.clf()

#plt.plot(U_A,Diff_I,':',color="lightcoral",label="Messwerte")
#plt.ylabel(r'$(I_\text{A}(U)-I_\text{A}(U+\Delta U))\,/\,\si{\nano\ampere}$')
#plt.xlabel(r'$U_\text{A}\,/\,\si{\volt}$')
#plt.grid(':')
#plt.legend()
#plt.savefig("../plots/EnergieDiff2.pdf")


np.savetxt('../data/energy.txt', np.column_stack([U_A, I_A, Diff_I]), header="U_A \t I_A \t Delta I_A")