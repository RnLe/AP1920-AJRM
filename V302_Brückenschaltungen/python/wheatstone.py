import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

#Bauteile
ave_R_2=[332.0, 500.0, 1000, 332.0, 500.0, 1000]
err_R_2=[0.7, 1.0, 2, 0.7, 1.0, 2]
R_2=unp.uarray(ave_R_2, err_R_2)

#Potentiometer
ave_R_3=[542,440,282,598,497,330]
err_R_3=[3,2,1,3,2,2]
R_3=unp.uarray(ave_R_3, err_R_3)
ave_R_4=[458,560,718,402,503,670]
err_R_4=[2,3,4,2,3,3]
R_4=unp.uarray(ave_R_4, err_R_4)

print(R_2*R_3/R_4)

#[392.89082969432314+/-2.891190145135515
# 392.85714285714283+/-2.869743760029788
# 392.7576601671309+/-2.7100620811868836
# 493.87064676616916+/-3.6414332047545988
# 494.0357852882704+/- 3.689279800128304
# 492.53731343283584+/-3.8398947662403753]