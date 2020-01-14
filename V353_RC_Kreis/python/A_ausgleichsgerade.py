import numpy as np
import matplotlib.pyplot as plt

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

t = np.genfromtxt("../data/A_times.csv",delimiter=",",unpack=True,usecols=0) #sind in 10^-3 s abgespeichert
U_C = np.genfromtxt("../data/A_lnU_C.csv",delimiter=",",unpack=True,usecols=0)

lnUNull=1.5686 #ln(4.8)
