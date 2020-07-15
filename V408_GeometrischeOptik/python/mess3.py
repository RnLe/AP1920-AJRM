import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from uncertainties import ufloat
import sys

S, A, l = np.genfromtxt('../data/mess3.csv', comments='#', unpack=True, delimiter=',')
plot = True if len(sys.argv) > 1 and sys.argv[1] == '-plot' else False

U = 29.4        # Ursprung
lr = 3          # Länge der Schablone

V = l / lr
g_ = A - U
b_ = S - A

g_x = 1+1/V
b_x = 1+V

params_g, cov_g = np.polyfit(g_x, g_, 1, cov=True)
uncertainties_g = np.sqrt(np.diag(cov_g))
params_b, cov_b = np.polyfit(b_x, b_, 1, cov=True)
uncertainties_b = np.sqrt(np.diag(cov_b))

fg = ufloat(params_g[0], uncertainties_g[0])
fb = ufloat(params_b[0], uncertainties_b[0])

uf = (fg+fb)/2

def printValues(f):
    f('\nHauptebene H\n')
    for name, value, uncertainty in zip('fh', params_g, uncertainties_g): 
        f(f'{name} = {value:8.1f} ± {uncertainty:.1f}\n')

    f('Hauptebene H\'\n')
    for name, value, uncertainty in zip('fh', params_b, uncertainties_b): 
        f(f'{name} = {value:8.1f} ± {uncertainty:.1f}\n')
    
    f(f'Gemeinsame Brennweite f = {uf}')

with open('../data/mess3.txt', 'w') as t:
    t.write('#g_ in cm,\tb_ in cm,\tg_x in cm,\tb_x in cm\n')
    for i in range(len(g_)):
        t.write(f'{g_[i]:.1f},\t{b_[i]:.1f},\t{g_x[i]:.1f},\t{b_x[i]:.1f}\n')
    printValues(t.write)

printValues(print)

if plot:
    mpl.use('pgf')
    mpl.rcParams.update({
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'pgf.texsystem': 'lualatex',
    'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}\usepackage{xfrac}',
    })

    def lin(x, a, b):
        return a*x + b
    x = np.linspace(np.min(g_x), np.max(g_x), 50)

    plt.plot(g_x, g_, '.', label='Messwerte', color='orange')
    plt.plot(x, lin(x, *params_g), label='Lineare Regression')
    plt.legend()
    plt.xlabel(r'$(1+\sfrac{1}{V})$\:/\:\si{\centi\meter}')
    plt.ylabel(r'$g$\'\:/\:\si{\centi\meter}')
    plt.tight_layout()
    plt.savefig('plotAbbe1')

    plt.close()

    x = np.linspace(np.min(b_x), np.max(b_x), 50)

    plt.plot(b_x, b_, '.', label='Messwerte', color='orange')
    plt.plot(x, lin(x, *params_b), label='Lineare Regression')
    plt.legend()
    plt.xlabel(r'$(1+V)$\:/\:\si{\centi\meter}')
    plt.ylabel(r'$b$\'\:/\:\si{\centi\meter}')
    plt.tight_layout()
    plt.savefig('plotAbbe2')