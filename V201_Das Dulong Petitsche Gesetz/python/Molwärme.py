import numpy as np

C_p=dict(tin=[30.9,30.9,32.0],alum=[24.8,21.1,25.9],copper=24.1)
alpha=dict(tin=27.0,alum=23.5,copper=16.8)
kappa=dict(tin=55,alum=75,copper=136)
V_0=dict(tin=16.3,alum=10.0,copper=7.09)
T_m=dict(tin=[296.05,295.85,295.45],alum=[297.15,296.85,296.65],copper=296.05)

C_V = dict(tin=[], alum=[], copper=0)

with open("data/Molwärme.txt", 'w') as f:
    f.write("Stoff\tMolwärme\n")
    for material in ["tin", "alum", "copper"]:
        if material is not "copper":
            f.write(f"{material}")
            for i in range(3):
                C_V[material].append(C_p[material][i]*1000 - 9*alpha[material]**2 *(1/(10**12)) *kappa[material]* 10**9 *V_0[material]* (1/(10**6)) *T_m[material][i])
                f.write(f"\t\t{round(C_V[material][i], 2)}\n")
        else:
            f.write(f"copper\t")
            C_V[material] = (C_p[material]*1000 - 9*alpha[material]**2 *(1/(10**12)) *kappa[material]* 10**9 *V_0[material]* (1/(10**6)) *T_m[material])
            f.write(f"{round(C_V[material], 2)}\n")
