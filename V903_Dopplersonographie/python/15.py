import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import scipy.constants as const
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

c0=const.physical_constants["speed of light in vacuum"]

nu0=2*10**6
numax=np.array([90,94,135,200,290])
nustd=np.array([49,61,85,110,146])
rpm=np.array([2000,2800,3600,4400,5200])

vmax=numax*c[0]/(2*nu0*np.cos(np.pi/12))
vstd=nustd*c[0]/(2*nu0*np.cos(np.pi/12))