#import numpy as np
import scipy.constants as const
from uncertainties import ufloat
#import sympy
#import uncertainties.unumpy as unp

#Konstanten
#e=const.physical_constants["elementary charge"]
h=const.physical_constants["Planck constant in eV s"]
c=const.physical_constants["speed of light in vacuum"]

E=ufloat(5.0,0.1) #in eV

print("Wellenlänge ist: ",h[0]*c[0]/E)