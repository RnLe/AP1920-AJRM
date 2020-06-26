import numpy as np
#import scipy.constants as const
from uncertainties import ufloat
#import sympy
#import uncertainties.unumpy as unp

#Konstanten
#e=const.physical_constants["elementary charge"]
#h=const.physical_constants["Planck constant"]
#c=const.physical_constants["speed of light in vacuum"]

N=np.array([129, 143, 144, 136, 139, 126, 158])
print('N Impulse innerhalb von 300 Sekunden:',N)
print('Der Mittelwert von N:',np.mean(N))
print('Der Messfehler von N:',np.std(N)*7/6) #Der Faktor 7/6 deshalb, weil bei np.std() die Standardabweichung (durch N teilen) und nicht der Messfehler (durch N-1 teilen) berechnet wird
print('Auf 300 Sekunden bezogen ist das eine Rate von:',np.mean(N)/300,'+-',np.std(N)*7/1800)
#Testcode:
#x=np.array([1,2])
#print("Test: ",x,'\n',np.mean(x),',\t',np.std(x))
m1=ufloat(0.0025295743304409282,0.0005284165097716055)
m2=ufloat(0.017656794692854992,0.0006296492943900561)
print(np.log(2)/m1)
print(np.log(2)/m2)