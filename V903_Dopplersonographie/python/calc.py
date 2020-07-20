import numpy as np
#import scipy.constants as const
#from uncertainties import ufloat
#import sympy
#import uncertainties.unumpy as unp

#Konstanten
#e=const.physical_constants["elementary charge"]
#h=const.physical_constants["Planck constant"]
#c=const.physical_constants["speed of light in vacuum"]

theta=np.array([np.pi/12,np.pi/6,np.pi/4])
c_L=1800 # in m/s
c_P=2700 # in m/s
faktor=2/3 # =c_L/c_P

alpha=np.pi/2-np.arcsin(np.sin(theta)*2/3)

print("Prismawinkel in Grad:\t",theta/(2*np.pi)*360,"\nDopplerwinkel in Grad:\t",alpha/(2*np.pi)*360)

#Reynoldszahl
eta=12*10**(-3)
rho=1.15*1000
d=0.01
vmax=np.array([92.3,41.4])*10**(-2)
Re=rho*vmax*d/eta
print("Reynoldszahl für die maximale Geschwindigkeit:\t",Re)