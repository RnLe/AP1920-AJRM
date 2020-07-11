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

#mu_B=0.5*e[0]*h[0]/(2*np.pi*m_e[0])  # Bohrsches Magneton
#print("\nBohrsches Magneton: ",mu_B)

names=["Nd","Gd","Dy"]
m=np.array([9.0,14.08,14.38])*10**(-3) # Masse in kg
rho=np.array([7.24,7.40,7.8])*10**3 # DIchte in kg/m^3

#Lande-Faktor --> Achtung, Köpfe runter, das Flugzeug landet
#g_J=(3*J*(J+1)+S*(S+1)-L*(L+1))/(2*J*(J+1))

#Länge der Spule
l=0.135 # in Meter

#effektive Querschnittsfläche in m^2
Q_eff=m/(l*rho)

R_3_Luft=2.58

R_3=np.array([2.73,3.47,4.16])
DeltaR=R_3-R_3_Luft

#Querschnitt Spule in m^2
F=86.6*10**(-6)

chi_R=2*DeltaR*F/(R_3*Q_eff)

#Speisespannung in volt
U_Sp=1
#Brückenspannung in volt
U_Br=np.array([1.45,1.35,1.15])*10**(-5)

chi_U=4*F*U_Br/(Q_eff*U_Sp)

chi_OU=4*1.5*10**(-5)/U_Sp

print("Unnötigerweise, aber trotzdem: Die Suszeptibilität ohne Füllung, berechnet mithilfe der Brückenpannung: ",chi_OU)

for i in range(3):
    print("\n",names[i],":\nChi über R:\t",chi_R[i],"\nChi über U:\t",chi_U[i])