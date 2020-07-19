import matplotlib.pyplot as plt
import numpy as np
#from uncertainties import ufloat
import scipy.constants as const
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

c=const.physical_constants["speed of light in vacuum"]

nu0=2*10**6
numax=np.array([-105,-145,-220,-330,-470])
nustd=np.array([-61,-85,-122,-165,-232])
rpm=np.array([2000,2800,3600,4400,5200])

vmax=numax*c[0]/(2*nu0*np.cos(np.pi/4))
vstd=nustd*c[0]/(2*nu0*np.cos(np.pi/4))

plt.plot(vmax,numax/np.cos(np.pi/4),"x",color='darkgreen',label='Messwerte')
plt.plot(vstd,nustd/np.cos(np.pi/4),"x",color='orange',label='Messwerte')
plt.ylabel(r'$\frac{\Delta \nu}{\cos \SI{45}{\degree}}\,/\,\si{\hertz}$')
plt.xlabel(r'$v\,/\,\si{\meter\per\second}$')
plt.grid(':')
plt.legend()
plt.savefig("../plots/45.pdf")

plt.clf()