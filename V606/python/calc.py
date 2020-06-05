import numpy as np
import scipy.constants as const
#from uncertainties import ufloat
#import sympy
#import uncertainties.unumpy as unp

#Konstanten
e=const.physical_constants["elementary charge"] # Elementarladung
h=const.physical_constants["Planck constant"] # Planck Konstante
#c=const.physical_constants["speed of light in vacuum"]
k_B=const.physical_constants["Boltzmann constant"] # Boltzmann in J/K
mu_0=const.physical_constants["mag. constant"] # magn. Permeabilität in N/A^2
m_e=const.physical_constants["electron mass"] # Masse eines Elektrons
n_A=const.physical_constants["Avogadro constant"] # Avogadro-Konstante
print("Elementarladung: ",e,"\nPlanckKonstante: ",h,"\nBoltzmannKonstante: ",k_B,"\nmagnetische Permeabilität: ",mu_0,"\nElektronmasse: ",m_e,"\nAvogadro-Konstante: ",n_A)

mu_B=0.5*e[0]*h[0]/(2*np.pi*m_e[0])  # Bohrsches Magneton
print("\nBohrsches Magneton: ",mu_B)

names=["Nd","Gd","Dy"]
m=np.array([9.0,14.08,14.38]) # Masse
rho=np.array([7.24,7.40,7.8]) # DIchte
J=np.array([4.5,-3.5,7.5]) # Gesamtdrehimpuls
L=np.array([6,0,5]) # Bahndrehimpuls
S=np.array([1.5,3.5,2.5]) # Spin
M=np.array([144.22,157.25,162.50]) # Molare Masse in g/mol aus Kohlrausch, S. 610
M_Sauerstoff=15.9994

M_Molekuel=3*M_Sauerstoff+2*M # Molare Masse der Molekülverbindung
N=2*n_A[0]*rho/M_Molekuel # Anzahl Ione pro Volumen in 1/cm^3

#Lande-Faktor --> Achtung, Köpfe runter, das Flugzeug landet
g_J=(3*J*(J+1)+S*(S+1)-L*(L+1))/(2*J*(J+1))

for i in range(3):
    print("\n",names[i],":\nMolare Masse des Moleküls:\t",M_Molekuel[i],"\nAnzahl der Ione pro VE:\t",N[i],"\nLande-Faktor:\t",g_J[i])


# Berechnung der Suszeptibilität theoretisch:
T=297
chi=mu_0[0]*mu_B**2*g_J**2*N*10**6*J*(J+1)/(3*k_B[0]*T)
print("Und die theoretischen Werte für die Suszeptibilität bei einer Temperatur von 297 Kelvin siiiiind:\n",chi)