import numpy as np
import scipy.constants as const
#from uncertainties import ufloat
#import sympy
#import uncertainties.unumpy as unp

#Konstanten
#e=const.physical_constants["elementary charge"]
#h=const.physical_constants["Planck constant"]
#c=const.physical_constants["speed of light in vacuum"]
k_B=const.physical_constants["Boltzmann constant"] # Boltzmann in J/K
mu_0=const.physical_constants["mag. constant"] # magn. Permeabilität in N/A^2


names=["Nd","Gd","Dy"]
m=np.array([9.0,14.08,14.38])
rho=np.array([7.24,7.40,7.8])
J=np.array([4.5,2.5,7.5])
L=np.array([6,6,5])
S=np.array([1.5,3.5,2.5])

#Lande-Faktor --> Achtung, Köpfe runter, das Flugzeug landet
g_J=(3*J*(J+1)+S*(S+1)-L*(L+1))/(2*J*(J+1))

