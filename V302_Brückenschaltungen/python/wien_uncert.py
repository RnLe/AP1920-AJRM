import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

R=ufloat(400,0.8)
C=ufloat(0.000000660,0.00000000132)
k=(2*np.pi)**(-1)

print(k*(R*C)**(-1))

# 602.9+/-1.7