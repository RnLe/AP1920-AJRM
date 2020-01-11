import numpy as np

t = np.genfromtxt("../data/Messreihe1_klKugel.csv",delimiter=",",unpack=True,usecols=0)
K_kl=0.07640*10**(-6) #in Pa m^3 kg^-1
m=4.4531*10**(-3)
d=15.6*10**(-3)
V=(4/3) * np.pi * (d/2)**3
rho_kl=m/V
rho_fl=997.2965 #Quelle: handbook, Dichte für 24°C

visk=K_kl*(rho_kl-rho_fl)*t
print(visk)
