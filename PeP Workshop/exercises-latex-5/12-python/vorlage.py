import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import (
    nominal_values as noms,
    std_devs as stds,
)

from curve_fit import ucurve_fit

def f(x, a, b, c, d):
    return a * np.sin(b*x + c) + d



def make_SI(num, unit, exp='', figures=None):
    ''' Format an uncertainties ufloat as a \SI quantity '''
    if np.any(stds([num])):
        if figures is None:
            figures = ''
        x = '{0:.{1:}uf}'.format(num, figures).replace('/', '')
    else:
        x = '{0:.{1:}f}'.format(num, figures)

    return r'\SI{{{}{}}}{{{}}}'.format(x, exp, unit)

    
t, U, y_err = np.genfromtxt("data.txt", unpack=True)



parameters, pcov = ucurve_fit(f, t, U, p0=[1, 1e3, 0, 0])

x = np.linspace(t[0], t[-1], 1000)

plt.plot(x, f(x, *parameters))
plt.show()