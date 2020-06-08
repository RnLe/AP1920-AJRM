import numpy as np

c_w = 4.18
c_gm_g = 219.1
m_k = dict(tin=203, alum=153, copper=237)
m_w = dict(tin=[642.76, 645.94, 659.46], alum=[654.63, 649.87, 669.27], copper=654.82)
T_w = dict(tin=[21.8, 21.6, 21.3], alum=[21.0, 21.3, 21.0], copper=20.9)
T_k = dict(tin=[83.3, 83.1, 75.8], alum=[87.2, 82.8, 75.1], copper=89.2)
T_m = dict(tin=[22.9, 22.7, 22.3], alum=[24.0, 23.7, 23.5], copper=22.9)

c_k = dict(tin=[], alum=[], copper=0)

with open("data/spezifischeWärme.txt", 'w') as f:
    f.write("Stoff\tSpezifische Wärme\n")
    for material in ["tin", "alum", "copper"]:
        if material is not "copper":
            f.write(f"{material}")
            for i in range(3):
                c_k[material].append((c_w*m_w[material][i] + c_gm_g)*(T_m[material][i]-T_w[material][i])/(m_k[material]*(T_k[material][i] - T_m[material][i]))) 
                #hier war jeweils eine Klammer zu wenig: (T_k - T_m) wurde nicht dividiert sondern multipliziert
                f.write(f"\t\t{round(c_k[material][i], 2)}\n")
        else:
            f.write(f"copper\t")
            c_k[material] = (c_w*m_w[material] + c_gm_g)*(T_m[material]-T_w[material])/(m_k[material]*(T_k[material] - T_m[material]))
            f.write(f"{round(c_k[material], 2)}\n")