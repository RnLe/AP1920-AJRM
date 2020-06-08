import numpy as np

ID, t1, t2, t3, t4, t5, t6, t7, t8, t = np.genfromtxt("../V204_Waermeleitf/Messung_1(statisch).txt", unpack=True)

# squash all temp arrays into another array. this helps for the iteration
temps = [t1, t2, t3, t4, t5, t6, t7, t8]

# the target values at which the temps are to be extracted
t_selected = [60, 150, 295, 475, 640]
# an new 2 dim array for the extracted values
temps_new = [[],[],[],[],[],[],[],[]]

i = 0
j = 0
while i < len(t_selected):
    # if the values match
    if t[j] == t_selected[i]:
        k = 0
        # iterate through and append the vlaues to the new array
        for y in temps:
            temps_new[k].append(y[j])
            k += 1
        i += 1
    j += 1


print(temps_new)

# brass wide
# close: T2, far: T1
# brass narrow
# close: T3, far: T4
# aluminum
# close: T6, far: T5
# stainless steel
# close: T7, far: T8

delta_T_brass_wide = []
delta_T_brass_narrow = []
delta_T_aluminum = []
delta_T_stainless_steel= []

i = 0
while i < len(t_selected):
    delta_T_brass_wide.append(temps_new[1][i]-temps_new[0][i])
    delta_T_brass_narrow.append(temps_new[2][i]-temps_new[3][i])
    delta_T_aluminum.append(temps_new[5][i]-temps_new[4][i])
    delta_T_stainless_steel.append(temps_new[6][i]-temps_new[7][i])
    i += 1

print(f"diff 1: {delta_T_brass_wide}\n diff 1: {delta_T_brass_narrow}\n diff 1: {delta_T_aluminum}\n diff 1: {delta_T_stainless_steel}\n")

# units in cm²
A_narrow = 0.000028
A_normal = 0.000048

# unit in cm
delta_x = 0.03

# kappa
k_brass = 112
k_aluminum = 221
k_edelstahl = 46

dQ_per_dt = [[], [], [], [], []]

i = 0
while i < len(t_selected):
    dQ_per_dt[i].append(A_normal/delta_x*delta_T_brass_wide[i]*k_brass)
    dQ_per_dt[i].append(A_narrow/delta_x*delta_T_brass_narrow[i]*k_brass)
    dQ_per_dt[i].append(A_normal/delta_x*delta_T_aluminum[i]*k_aluminum)
    dQ_per_dt[i].append(A_normal/delta_x*delta_T_stainless_steel[i]*k_edelstahl)
    i += 1

print(dQ_per_dt)