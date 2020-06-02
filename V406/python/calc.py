import numpy as np
import scipy.constants as const
from uncertainties import ufloat
import sympy
import uncertainties.unumpy as unp

#Konstanten
e=const.physical_constants["elementary charge"]
h=const.physical_constants["Planck constant"]
c=const.physical_constants["speed of light in vacuum"]

#Berechnung der Plateau-Schwankung
m=ufloat(0.02304381096115296,0.0032885015034107745)
b=ufloat(157.8974444189741,1.70973970134535573)
print("Plateau-Schwankung um den Idealwert innerhalb von 100 Volt:", 50*m/(m*510+b))

#Berechnung Fehler Zwei-Quellen
N=np.array([96401,158479,76518])
N_err=np.sqrt(N)
N_rate=N/120
N_rate_err=N_err/120
print("Impulse:",N,"+-",N_err,"\nImpulsrate:",N_rate,"+-",N_rate_err)

N1=ufloat(N_rate[0],N_rate_err[0])
N3=ufloat(N_rate[1],N_rate_err[1])
N2=ufloat(N_rate[2],N_rate_err[2])

print("Totzeit:\nplus:",1/N3+unp.sqrt(1/(N3**2)-(N1+N2-N3)/(N1*N2*N3)),"\nminus:",1/N3-unp.sqrt(1/(N3**2)-(N1+N2-N3)/(N1*N2*N3)))
print("Totzeit gemäß Anleitung:", (N1+N2-N3)/(2*N1*N2))

#Anodenstrom Zählrohrstrom
I=np.array([0.3,0.4,0.7,0.8,1.0,1.3,1.4,1.8])*10**(-6) #Strom in Ampere
errI=np.array([5,5,5,5,5,5,5,5])*10**(-8) #Strom Fehler
uI=unp.uarray(I,errI)
Nt=np.array([9837 ,9995 ,10264,10151,10184,10253,10493,11547]) #Anzahl Impulse
uNt=unp.uarray(Nt,np.sqrt(Nt)) # Anzahl Impulse mit Fehler
uNn=uNt/60 #Rate mit Fehler
e0=e[0]

#Z=uI/(uNn*e0)
print("Anzahl Elektronen Z",uI/(uNn*e0))
print("Impulsrate mit Fehler",uNn)
print("Impulse mit Fehler",uNt)