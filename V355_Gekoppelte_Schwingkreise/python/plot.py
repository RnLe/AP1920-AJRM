import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

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

f_minus = [33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1]
f_plus = [81.3,61.1,57.1,48.7,44.7,42.8,41.4,40.2]
c_k = [1.0 ,2.2 ,2.7 ,4.7 ,6.8 ,8.2 ,10.0,12.0]
cur = [38.12,40.83,39.22,42.70,45.00,38.12,42.29,41.66]

x = np.linspace(1, 12, 200)

fig, ax = plt.subplots()
ax2 = ax.twinx()


ax2.plot(c_k, cur, 'g^')
ax.plot(c_k, f_minus, 'x')
ax.plot(c_k, f_plus, 'o')
ax.plot(c_k, f_minus, 'b')

ax.set_xlabel(r'$C_k /$ nF')
ax.set_ylabel(r'$f /$ kHz', color='orangered')
ax.tick_params(axis='y', labelcolor='orangered')
ax2.set_ylabel(r'$I /$ mA', color='g')
ax2.tick_params(axis='y', labelcolor='g')

ax.legend(['1. Fundamentalschwingung', '2. Fundamentalschwingung'], loc=2, bbox_to_anchor=(0.5, 0.9))
ax2.legend([r'Strom $I_2$'])

fig.tight_layout(pad=0, h_pad=1.12, w_pad=1.12)
plt.savefig('../plots/Messdaten.pdf')