import numpy as np
from uncertainties import ufloat

S, Ln, Lf = np.genfromtxt('../data/mess2.csv', comments='#', unpack=True, delimiter=',')

U = 29.4        # Ursprung

gn = Ln - U
bn = S - Ln
gf = Lf - U
bf = S - Lf
dn = abs(gn-bn)
df = abs(gf-bf)
e = S - U

# fn, ff = [], []
# for i in range(len(e)): fn.append((e[i]**2 - dn[i]**2) / 4*e[i])
# for i in range(len(e)): ff.append((e[i]**2 - df[i]**2) / 4*e[i])

fn = (e**2 - dn**2) / (4*e)
ff = (e**2 - df**2) / (4*e)
ufn = ufloat(np.mean(fn), np.std(fn))
uff = ufloat(np.mean(ff), np.std(ff))
uf = (ufn + uff) / 2

with open('../data/mess2.txt', 'w') as t:
    t.write('#g_n in cm,\tb_n in cm,\tg_f in cm,\tb_f in cm,\te in cm,\td_n in cm,\td_f in cm,\tfn in cm,\tff in cm\n')
    for i in range(len(gn)):
        t.write(f'{gn[i]:.1f},\t{bn[i]:.1f},\t{gf[i]:.1f},\t{bf[i]:.1f},\t{e[i]:.1f},\t{dn[i]:.1f},\t{df[i]:.1f},\t{fn[i]:.1f},\t{ff[i]:.1f}\n')

    t.write(f'\nf = {uf}')
    t.write(f'\nfn = {ufn}')
    t.write(f'\nff = {uff}')

print(uf)