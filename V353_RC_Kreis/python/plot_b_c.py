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

data = np.genfromtxt('data/Messdaten_b_und_c.txt', comments='#')
amplituden = []
frequenz = []
phase = []

for i in range(len(data)-1):
    frequenz.append(data[i][0])
    amplituden.append(data[i][1]/2.7)
    phase.append(data[i][4])

x = np.linspace(frequenz[0], frequenz[-2], 200)

plt.plot(frequenz, amplituden, 'x')
plt.plot(frequenz, phase, '.')
plt.xlabel(r'$f / \mathrm{Hz}$')
plt.ylabel(r'Verhältnis')
plt.legend(['Amplitude', 'Phase'])

plt.savefig('plots/plot_b_c.pdf')