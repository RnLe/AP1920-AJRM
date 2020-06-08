import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

ave_L_2=[14.6,14.6,14.6]
err_L_2=[0.03,0.03,0.03]
L_2=unp.uarray(ave_L_2, err_L_2)
ave_R_2=[332.0,500.0,664]
err_R_2=[0.7,1.0,1]
R_2=unp.uarray(ave_R_2, err_R_2)
ave_R_3=[255,185,145]
err_R_3=[1,1,1]
R_3=unp.uarray(ave_R_3, err_R_3)
ave_R_4=[745,815,855]
err_R_4=[4,4,4]
R_4=unp.uarray(ave_R_4, err_R_4)

print('Indu.-Messbrücke')
print('R_x')
print(R_2*R_3/R_4)
print('L_x')
print(L_2*R_3/R_4)

C_4=ufloat(750,2)
CR_2=ufloat(664,1)
CR_3=ufloat(57,2)
CR_4=ufloat(270,8)

print('Maxwell-Messbrücke')
print('R_x')
print(CR_2*CR_3/CR_4)
print('L_x')
print(C_4*CR_2*CR_3) #nano=10^-9 

# Indu.-Messbrücke
# R_x
# [113.63758389261746+/-0.7926310969134958
#  113.49693251533742+/-0.8591847533314321
#  112.60818713450293+/-0.9536365169985564]
# L_x
# [4.99731543624161+/-  0.03477658034168615
#  3.3141104294478527+/-0.0251367818090794
#  2.4760233918128653+/-0.021252255949433144]
# Maxwell-Messbrücke
# R_x
# 140+/-6
# L_x
# (2.84+/-0.10)e+07 
