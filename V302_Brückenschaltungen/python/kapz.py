import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

ave_C_2=[450,597,992,597,992,750]
err_C_2=[1,1,2,1,2,2]
C_2=unp.uarray(ave_C_2, err_C_2)

ave_R_3=[408,487,611,595,711,643]
err_R_3=[1,1,1,1,1,1]
R_3=unp.uarray(ave_R_3, err_R_3)
ave_R_4=[592,513,389,405,289,377]
err_R_4=[1,1,1,1,1,1]
R_4=unp.uarray(ave_R_4, err_R_4)

print(C_2*R_4/R_3)

#[652.9411764705883+/-2.42547536028391
# 628.8726899383984+/-2.068791160901737
# 631.5679214402619+/-2.3077654568111856
# 406.3613445378151+/-1.391575876042266
# 403.2180028129395+/-1.7114678345845904
# 439.7356143079316+/-1.7897645144451908]