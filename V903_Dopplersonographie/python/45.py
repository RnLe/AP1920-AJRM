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
theta=np.pi/4
alpha=np.pi/2-np.arcsin(np.sin(theta)*2/3)
nu0=2*10**6
numax=np.array([105,145,220,330,470])
nustd=np.array([61,85,122,165,232])
rpm=np.array([2000,2800,3600,4400,5200])

vmax=numax*c[0]/(2*nu0*np.cos(alpha))
vstd=nustd*c[0]/(2*nu0*np.cos(alpha))

plt.plot(vmax,numax/np.cos(alpha),"x",color='darkgreen',label=r'$\Delta \nu_\text{max}$')
plt.plot(vstd,nustd/np.cos(alpha),"x",color='orange',label=r'$\Delta \nu_\text{std}$')
plt.ylabel(r'$\frac{| \Delta \nu |}{\cos \alpha}\,/\,\si{\hertz}$')
plt.xlabel(r'$| v_\text{rech} |\,/\,\si{\meter\per\second}$')
plt.grid(':')
plt.legend()
plt.savefig("../plots/45_1.pdf")

plt.clf()

plt.plot(rpm,numax/np.cos(alpha),"x",color='darkgreen',label=r'$\Delta \nu_\text{max}$')
plt.plot(rpm,nustd/np.cos(alpha),"x",color='orange',label=r'$\Delta \nu_\text{std}$')
plt.ylabel(r'$\frac{| \Delta \nu |}{\cos \alpha}\,/\,\si{\hertz}$')
plt.xlabel(r'$| v_\text{mess} |\,/\,\mathrm{rpm}$')
plt.grid(':')
plt.legend()
plt.savefig("../plots/45_2.pdf")
