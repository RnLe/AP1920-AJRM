import numpy as np
import matplotlib.pyplot as plt

time = np.genfromtxt("../data/Ave_Temp_großeKugel.csv",delimiter=",",unpack=True,usecols=0)
Temp = np.genfromtxt("../data/Temp.csv",delimiter=",",unpack=True,usecols=0)
m=4.9528*10**(-3)
d=15.76*10**(-3)
V=(4/3) * np.pi * (d/2)**3
rho_kl=m/V
rho_Fl=np.array([997.2965,995.0262,994.0319,992.5943,991.4364,989.7914,987.5809,985.6952,983.1989,981.0951])
visk=1.173219*10**(-3)

K_gr=visk/((rho_kl-rho_Fl)*time)
K=np.mean(K_gr)
K_std=np.std(K_gr)

print(K) #Berechnung der Gerätekonstante K_gr für T=23.5
print(K_std)

#ab hier:Berechnung der Viskosität in Abhängigkeit der Temperatur
Vis_Temp=K*(rho_kl-rho_Fl)*time
print(Vis_Temp)

#Polyfit von der Andrade-Gleichung
ln_eta=np.log(Vis_Temp) #np.log ist der natürliche Logarithmus ln
Temp=Temp+273.15 #Umrechnung Celsius-->Kelvin
Temp_hoch_minus_eins=Temp**(-1)

plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 2

#plt.plot(Temp_hoch_minus_eins,ln_eta,'k.',label="Messwerte")
#plt.savefig("Messwerte.pdf")
#plt.clf()

params, covariance_matrix = np.polyfit(Temp_hoch_minus_eins, ln_eta, deg=1, cov=True) #linearer Fit

errors = np.sqrt(np.diag(covariance_matrix))

#Ausgabe der Koeffizienten der 'linearen' Funktion: ln(eta)=ln(A) + B*(1/T)
#a entspricht B, b entspricht ln(A)
for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}') 

x_plot = np.linspace(2.95*10**(-3), 3.4*10**(-3))
plt.plot(Temp_hoch_minus_eins, ln_eta, '.', label="Messwerte")
plt.plot(
    x_plot,
    params[0] * x_plot + params[1],
    label='Lineare Regression',
    linewidth=3,
)
plt.legend(loc="best")

#Es gibt keine Probleme beim Durchlaufen des Programms, bis auf bei savefig... keine Ahnung warum.
#plt.savefig('plot_2.pdf')
