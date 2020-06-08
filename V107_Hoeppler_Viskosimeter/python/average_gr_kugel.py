import numpy as np
import matplotlib.pyplot as plt

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

fallzeiten = np.genfromtxt('../data/Messreihe2_grKugel.csv', delimiter=',')
fallzeiten_kl = np.genfromtxt('../data/Messreihe1_klKugel.csv', delimiter=',')
temps = np.genfromtxt('../data/Temp.csv')
ffallzeiten = []
ffallzeiten_kl = []

arith_mitt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
std_abw = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

arith_m = 0
std_abw_kl = 0

for i in range(100): #durch die Formattierun der csv datei gibt es quasi 50 Zeilen. je 5 Zeilen sind also ein Temperaturblock. 1 Zeile hat 2 Messwerte
    ffallzeiten.append(fallzeiten[(int)(i/2)][i%2])

for i in range(100):
    arith_mitt[(int)(i/10)] += ffallzeiten[i]
    if ((i+1) % 10 == 0): 
        arith_mitt[(int)(i/10)] /= 10
        arith_mitt[(int)(i/10)] = round(arith_mitt[(int)(i/10)], 3)

for i in range(100): 
    std_abw[(int)(i/10)] += (ffallzeiten[i]-arith_mitt[(int)(i/10)])**2
    if ((i+1) % 10 == 0):
        std_abw[(int)(i/10)] /= 10
        std_abw[(int)(i/10)] = round(np.sqrt(std_abw[(int)(i/10)]), 3)

for i in range(10): 
    ffallzeiten_kl.append(fallzeiten_kl[(int)(i/2)][i%2])

for val in ffallzeiten_kl:
    arith_m += val

arith_m /= 10
arith_m = round(arith_m, 3)

for val in ffallzeiten_kl:
    std_abw_kl += (val-arith_m)**2

std_abw_kl /= 10
std_abw_kl = round(np.sqrt(std_abw_kl), 3)

plt.errorbar(temps, arith_mitt, yerr=std_abw, fmt='.')
plt.xlabel(r'Temperatur $T /$ °C')
plt.ylabel(r'Fallzeit $t /$ s')
plt.xticks(temps, temps)


plt.tight_layout(pad=0, h_pad=1.12, w_pad=1.12)
plt.savefig('../plots/avg_gr.pdf')

with open("../data/fehlerrechnung_gr.txt", 'w') as f:
    f.write("Temperatur\tArithmetisches Mittel\tStandardabweichung\n")
    for i in range(10):
        f.write(f'{temps[i]}\t\t{arith_mitt[i]}\t\t\t{std_abw[i]}\n')
    f.write("\nKleine Kugel\n")
    f.write("Temperatur\tArithmetisches Mittel\tStandardabweichung\n")
    f.write(f"{temps[0]}\t\t{arith_m}\t\t\t{std_abw_kl}\n")
    



print(arith_mitt)
print(std_abw)