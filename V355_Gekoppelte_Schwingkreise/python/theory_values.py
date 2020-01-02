import numpy as np

f_plus = [81.3,61.1,57.1,48.7,44.7,42.8,41.4,40.2]
f_minus = [33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1]
C_k_in_nano = [1.0 ,2.2 ,2.7 ,4.7 ,6.8 ,8.2 ,10.0,12.0]
U_minus = [1.830,1.960,1.883,2.050,2.160,1.830,2.030,2.000]
R = 48
C_sp_in_nano = 0.037
C_in_nano = 0.8015
L_in_milli = 32.351
vol_180 = 9
vol_0 = 7.2

f_plus_theo = []
f_minus_theo = []
cur_theo = []
I2_plus_theo = []
I2_minus_theo = []
I2_theo = 0
I2 = []

for cap in C_k_in_nano:
    f_plus_theo.append(1 / (2*np.pi*np.sqrt(L_in_milli*(C_in_nano+C_sp_in_nano)*10**(-12))))

for cap in C_k_in_nano:
    f_minus_theo.append(1 / (2*np.pi*np.sqrt(L_in_milli*((C_in_nano*cap/(2*C_in_nano+cap))+C_sp_in_nano)*10**(-12))))

for i in range(len(U_minus)):
    I2_minus_theo.append(U_minus[i]*(1/(R*np.sqrt(4+((R**2*C_k_in_nano[i]**2/(L_in_milli*C_in_nano))*(10**-6)*(1+C_in_nano/C_k_in_nano[i]))))))

print(((R**2*C_k_in_nano[0]**2/(L_in_milli*C_in_nano))*(10**-6)*(1+C_in_nano/C_k_in_nano[0])))

I2_theo = vol_180/(2*R)

for vol in U_minus:
    I2.append(vol/R)

print("f_plus_theo = ")
for val in f_plus_theo:
    print(val)
#print(f_plus_theo)
print("\nf_minus_theo = ")
for val in f_minus_theo:
    print(val)
#print(f_minus_theo)
print("\nI2_minus_theo = ")
for val in I2_minus_theo:
    print(val*1000)
#print(I2_minus_theo)
print("\nI2 = ")
for val in I2:
    print(val*1000)
print("\nI2_theo = ")
print(I2_theo)