import numpy as np
#import scipy.constants as const
#from uncertainties import ufloat
#import sympy
#import uncertainties.unumpy as unp

#Konstanten
#e=const.physical_constants["elementary charge"] # Elementarladung
#h=const.physical_constants["Planck constant"] # Planck Konstante
#c=const.physical_constants["speed of light in vacuum"]
#k_B=const.physical_constants["Boltzmann constant"] # Boltzmann in J/K
#mu_0=const.physical_constants["mag. constant"] # magn. Permeabilität in N/A^2
#m_e=const.physical_constants["electron mass"] # Masse eines Elektrons
#n_A=const.physical_constants["Avogadro constant"] # Avogadro-Konstante
#print("Elementarladung: ",e,"\nPlanckKonstante: ",h,"\nBoltzmannKonstante: ",k_B,"\nmagnetische Permeabilität: ",mu_0,"\nElektronmasse: ",m_e,"\nAvogadro-Konstante: ",n_A)

d=np.array([3.72,1.93,4.75,1.75,3.00])*10**(-3)
z=np.array([2256,2133,3000,1135,1831])

lam=2*d/5.017/z
print("reskalierte Länge: ",d*10**3/5.017)
print("Wellenlänge: ",lam)
print("Mittelwert: ",np.mean(lam))
print("Messfehler: ",np.std(lam)*np.sqrt(5/4))

d2=np.array([3.72,4.75,1.75,3.00])*10**(-3)
z2=np.array([2256,3000,1135,1831])

lam2=2*d2/5.017/z2
print("Runde 2: Wellenlänge: ",lam2)
print("Runde 2: Mittelwert: ",np.mean(lam2))
print("Runde 2: Messfehler: ",np.std(lam2)*np.sqrt(4/3))

z3=np.array([33,32])
b=50*10**(-3)
wavelength=635*10**(-9)
DelP=0.8*10**5
p_0=1.0132*10**5
n=1+z3*wavelength*p_0/(2*b*DelP)

print("Brechindex: ",n)

n2=np.array([n[0],n[0],n[1],n[1],n[0]])
print("Mittelwert: ",np.mean(n2))
print("Messfehler: ",np.std(n2)*np.sqrt(5/4))