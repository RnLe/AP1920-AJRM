import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp


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

# Viskosität
m_kl = 4.4531e-3
m_gr = 4.9528e-3
d_kl = 15.6e-3
d_gr = 15.76e-3
Vol_kl = ((4/3) * np.pi * (d_kl/2)**3)  # m³
Vol_gr = ((4/3) * np.pi * (d_gr/2)**3)  # m³
dichte_kl = m_kl/Vol_kl
dichte_gr = m_gr/Vol_gr
dichte_w_raum = 997.538
dichte_w_dyn = np.genfromtxt('../data/dichte_literatur.txt', comments='#')
fallzeit_kl = ufloat(12.355, 0.137)
fallzeit_gr_nom = [91.910,71.087,67.227,61.661,57.571,53.458,49.012,45.809,43.047,40.338]
fallzeit_gr_err = [0.538,0.812,1.124,0.304,0.301,0.339,0.487,0.255,0.314,0.122]
fallzeit_gr = unp.uarray(fallzeit_gr_nom, fallzeit_gr_err)
geschw_kl = 0.1/fallzeit_kl
geschw_gr = 0.1/fallzeit_gr
K_kl = 0.07640e-06                                              # Pa m^3 kg^-1
K_gr = ufloat(1.4984678723241853e-08, 3.3706257564216015e-09)   # Pa m^3 kg^-1

visk_kl = K_kl*(dichte_kl-dichte_w_raum)*fallzeit_kl            # Viskosität von Wasser bei Raumtemperatur über kleine Kugel
K_gr = visk_kl/((dichte_gr-dichte_w_raum)*fallzeit_gr[0])       # Gerätekonstante der großen Kugel

visk_gr = K_gr*(dichte_gr-dichte_w_dyn)*fallzeit_gr

reynold_kl = (dichte_w_raum*geschw_kl*d_kl)/visk_kl
reynold_gr = (dichte_w_dyn*geschw_gr*d_gr)/visk_gr

print(reynold_kl)
print(geschw_kl)

temps = np.genfromtxt('../data/Temp.csv')

visko_theo = np.genfromtxt('../data/viskosität_literatur.txt', comments='#', delimiter=',')

viskosität_theo_x = visko_theo[1]
viskosität_theo_y = visko_theo[0]

def vis_f(x, a, b, c):
    return (a * 1/(x-b)) + c

params, cov = curve_fit(vis_f, viskosität_theo_x, viskosität_theo_y)

with open("../data/visko_theo.txt", 'w') as f:
    f.write("Theoriewerte für die Viskosität von Wasser mit curvefit\n")
    f.write("Temperatur\tViskosität in e-6 kg/(m*s)\n")
    for i in range(len(temps)):
        f.write(f'{temps[i]}\t\t{round(vis_f(temps[i], *params), 3)}\n')

with open("../data/visko_ger_reyn.txt", 'w') as f:
    f.write(f"Viskosität der kleinen Kugel {visk_kl*10**6}\n")
    f.write(f"Viskositäten der großen Kugel\n {str(visk_gr*10**6).strip('[]')}\n")
    f.write(f"\nGerätekonstante der kleinen Kugel {K_kl}\n")
    f.write(f"Gerätekonstante der großen Kugel {K_gr}\n")
    f.write(f"\nFallgechwindigkeit der kleinen Kugel {geschw_kl*10**3}\n")
    f.write(f"Fallgechwindigkeiten der großen Kugel\n {str(geschw_gr*10**3).strip('[]')}\n")
    f.write(f"\nReynoldzahl der kleinen Kugel {reynold_kl}\n")
    f.write(f"Reynoldzahlen der großen Kugel\n {str(reynold_gr).strip('[]')}\n")
    f.write(f"\nParameter a = {int(params[0])}, b = {int(params[1])}, c = {int(params[2])}\n")

plt.plot(temps, unp.nominal_values(visk_gr)*10**6, '.')
plt.plot(temps, vis_f(temps, *params), '.')

plt.xlabel(r'Temperatur $T / $°C')
plt.ylabel(r'Viskosität $\eta / \text{kg}\:\text{m}^{-1}\:\text{s}^{-1}10^{-6}$')
plt.legend(['Messwerte', 'Literaturwerte'])
plt.tight_layout(pad=0, h_pad=1.12, w_pad=1.12)
plt.savefig('../plots/visk_theo.pdf')