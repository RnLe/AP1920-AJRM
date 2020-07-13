import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

L, S = np.genfromtxt('../data/mess1.csv', comments='#', unpack=True, delimiter=',')

U = 29.4        # Ursprung

g = L - U
b = S - L
f = (g*b)/(g+b)
f_m = np.mean(f)
f_s = np.std(f)
uf = ufloat(f_m, f_s)

with open('../data/mess1.txt', 'w') as t:
    t.write('#g_i in cm,\tb_i in cm,\tf in cm\n')
    for i in range(len(g)):
        t.write(f'{np.round(g[i], 1)},\t{np.round(b[i], 1)},\t{np.round(f[i], 2)}\n')

    t.write(f'\nf = {uf}')

print(uf)

mpl.use('pgf')
mpl.rcParams.update({
'font.family': 'serif',
'text.usetex': True,
'pgf.rcfonts': False,
'pgf.texsystem': 'lualatex',
'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}',
})

for i in range(len(g)):
    plt.plot([0, b[i]], [g[i], 0])

plt.plot(f_m, f_m, 'k.', label='Brennweite')
plt.hlines(16.31, 0, 16.31, linestyles='dashed')
plt.vlines(16.31, 0, 16.31, linestyles='dashed')
plt.xticks([10, 16.31, 30, 40, 50, 60, 70])     # blöd. aber die 20 ist im Weg
plt.yticks([10, 16.31, 30, 40, 50, 60, 70])
plt.xlabel(r'$b_{i}$\:/\:\si{\centi\meter}')
plt.ylabel(r'$g_{i}$\:/\:\si{\centi\meter}')
plt.ylim(0)
plt.xlim(0)
plt.legend()
plt.tight_layout()
plt.savefig('plot1')