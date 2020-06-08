import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.optimize import curve_fit
import cmath

mpl.use('pgf')
mpl.rcParams.update({
'font.family': 'serif',
'text.usetex': True,
'pgf.rcfonts': False,
'pgf.texsystem': 'lualatex',
'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}',
})

I2 = np.genfromtxt('../data/Messdaten_V406_2.txt', comments='#', unpack=True)
I2[1] = I2[1]*10**-6
lam = 633*10**-6
_b = 0.15
_a = 0.75
_k = 2*np.pi/lam
_d = 626.1

def B_phi2(x, x0, a, b, c):
    return a * np.sinc(b*(x-x0))**2 + c

params, cov = curve_fit(B_phi2, I2[0], I2[1], p0=[12, 1, 1, 1])
x1 = np.linspace(0, I2[0][-1], 200)
plt.plot(I2[0], I2[1], 'b.')
plt.plot(x1, B_phi2(x1, *params))

uncertainties = np.sqrt(np.diag(cov))

for name, value, uncertainty in zip('xabc', params, uncertainties): 
    print(f'{name} = {value:8.8f} ± {uncertainty:.8f}')
print(params)
plt.savefig('plot2.pdf')