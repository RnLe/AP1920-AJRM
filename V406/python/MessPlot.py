import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.optimize import curve_fit

mpl.use('pgf')
mpl.rcParams.update({
'font.family': 'serif',
'text.usetex': True,
'pgf.rcfonts': False,
'pgf.texsystem': 'lualatex',
'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}',
})

I = np.genfromtxt('../data/Messdaten_V406_1.txt', comments='#', unpack=True)
I[1] = I[1]*10**-6
lam = 633*10**-9
b = 0.15*10**-3
a = 0.75*10**-3
k = 2*np.pi/lam
d = 626.1*10**-3
plt.plot(I[0], I[1], 'b.')

def B_phi2(x, x0, b, c, d):
    return d * np.sinc(b*(x-x0))**2 + c

p0 = np.genfromtxt('../data/p0.txt', unpack=True)
print(p0)

params, cov = curve_fit(B_phi2, I[0], I[1], p0=p0)

x = np.linspace(I[0][0], I[0][-1], 300)
plt.plot(x, B_phi2(x, *params))

with open('../data/p0.txt', 'w') as f:
    for p in params:
        f.write(f'{p}\n')
print(params)
plt.savefig('plot.pdf')