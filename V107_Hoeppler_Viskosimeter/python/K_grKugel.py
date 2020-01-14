import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit

import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
mpl.rcParams.update({
'font.family': 'serif',
'text.usetex': True,
'pgf.rcfonts': False,
'pgf.texsystem': 'lualatex',
'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}',
})

time = np.genfromtxt("../data/Ave_Temp_großeKugel.csv",delimiter=",",unpack=True,usecols=0)
Temp = np.genfromtxt("../data/Temp.csv",delimiter=",",unpack=True,usecols=0)
m=4.9528*10**(-3)
d=15.76*10**(-3)
V=(4/3) * np.pi * (d/2)**3
rho_kl=m/V
rho_Fl=np.array([997.2965,995.0262,994.0319,992.5943,991.4364,989.7914,987.5809,985.6952,983.1989,981.0951])
visk=1.173219*10**(-3)

K_gr=ufloat(1.4984678723241853e-08, 3.3706257564216015e-09)
# K=np.mean(K_gr)
# K_std=np.std(K_gr)

# print(K) #Berechnung der Gerätekonstante K_gr für T=23.5
# print(K_std)

fallzeit_gr_nom = [91.910,71.087,67.227,61.661,57.571,53.458,49.012,45.809,43.047,40.338]
fallzeit_gr_err = [0.538,0.812,1.124,0.304,0.301,0.339,0.487,0.255,0.314,0.122]
fallzeit_gr = unp.uarray(fallzeit_gr_nom, fallzeit_gr_err)

#ab hier:Berechnung der Viskosität in Abhängigkeit der Temperatur
Vis_Temp=K_gr*(rho_kl-rho_Fl)*fallzeit_gr
print(Vis_Temp)

#Polyfit von der Andrade-Gleichung
ln_eta=unp.log(Vis_Temp) #np.log ist der natürliche Logarithmus ln
Temp=Temp+273.15 #Umrechnung Celsius-->Kelvin
Temp_hoch_minus_eins=Temp**(-1)

#plt.plot(Temp_hoch_minus_eins,ln_eta,'k.',label="Messwerte")
#plt.savefig("Messwerte.pdf")
#plt.clf()

def func_lin(x, a, b):
    return a + b*x

params, covariance_matrix = curve_fit(func_lin, Temp_hoch_minus_eins, unp.nominal_values(ln_eta))
#params, covariance_matrix = np.polyfit(Temp_hoch_minus_eins, unp.nominal_values(ln_eta), deg=1, cov=True) #linearer Fit

errors = np.sqrt(np.diag(covariance_matrix))
print(covariance_matrix)
print(np.diag(covariance_matrix))
#Ausgabe der Koeffizienten der 'linearen' Funktion: ln(eta)=ln(A) + B*(1/T)
#a entspricht B, b entspricht ln(A)
for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}') 


ln_a = ufloat(-12.811, 0.237)
ln_a = np.e**ln_a

print(ln_a)
print(params[0])
print(params[1])

x_plot = np.linspace(2.95*10**(-3), 3.4*10**(-3))
plt.plot(Temp_hoch_minus_eins, unp.nominal_values(ln_eta), '.', label="Messwerte")
plt.plot(
    x_plot,
    params[1] * x_plot + params[0],
    label='Lineare Regression',
    linewidth=3,
)
plt.xlabel(r'$1 / T$')
plt.ylabel(r'ln$(\eta)$')

#Es gibt keine Probleme beim Durchlaufen des Programms, bis auf bei savefig... keine Ahnung warum.
# fix: es fehlte wieder die Einbindung der tex-header [RL]
plt.tight_layout(pad=0, h_pad=1.12, w_pad=1.12)
plt.savefig('../plots/plot_2.pdf')
