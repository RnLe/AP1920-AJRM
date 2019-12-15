import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

ave_wheat1=[393,393,393]
err_wheat1=[3,3,3]
wheat1=unp.uarray(ave_wheat1,err_wheat1)
ave_wheat2=[494,494,493]
err_wheat2=[4,4,4]
wheat2=unp.uarray(ave_wheat2,err_wheat2)
ave_kapz1=[653,629,632]
err_kapz1=[2,2,2]
kapz1=unp.uarray(ave_kapz1,err_kapz1)
ave_kapz2=[406,403,440]
err_kapz2=[1,2,2]
kapz2=unp.uarray(ave_kapz2,err_kapz2)
ave_induR=[114,113,113]
err_induR=[1,1,1]
induR=unp.uarray(ave_induR,err_induR)
ave_induL=[5.00,3.31,2.48]
err_induL=[0.04,0.03,0.02]
induL=unp.uarray(ave_induL,err_induL)

sum=0
for i in range(3):
    sum = sum + wheat1[i]
    if i==2: 
        ave=(1/3)*sum
        print(ave)
sum=0
for i in range(3):
    sum = (ave - wheat1[i])**2
    if i==2: 
        ave=((1/2)*sum)**(1/2)
        print(ave)
sum=0
for i in range(3):
    sum = sum + wheat2[i]
    if i==2: 
        ave=(1/3)*sum
        print(ave)
sum=0
for i in range(3):
    sum = (ave - wheat2[i])**2
    if i==2: 
        ave=((1/2)*sum)**(1/2)
        print(ave)
sum=0
for i in range(3):
    sum = sum + kapz1[i]
    if i==2: 
        ave=(1/3)*sum
        print(ave)
sum=0
for i in range(3):
    sum = (ave - kapz1[i])**2
    if i==2: 
        ave=((1/2)*sum)**(1/2)
        print(ave)
sum=0
for i in range(3):
    sum = sum + kapz2[i]
    if i==2: 
        ave=(1/3)*sum
        print(ave)
sum=0
for i in range(3):
    sum = (ave - kapz2[i])**2
    if i==2: 
        ave=((1/2)*sum)**(1/2)
        print(ave)
sum=0
for i in range(3):
    sum = sum + induR[i]
    if i==2: 
        ave=(1/3)*sum
        print(ave)
sum=0
for i in range(3):
    sum = (ave - induR[i])**2
    if i==2: 
        ave=((1/2)*sum)**(1/2)
        print(ave)
sum=0
for i in range(3):
    sum = sum + induL[i]
    if i==2: 
        ave=(1/3)*sum
        print(ave)
sum=0
for i in range(3):
    sum = (ave - induL[i])**2
    if i==2: 
        ave=((1/2)*sum)**(1/2)
        print(ave)

# 393.0+/-1.7
# 0.0+/-nan
# 493.7+/-2.3
# 0.5+/-2.3
# 638.0+/-1.2
# 4.2+/-1.2
# 416.3+/-1.0
# 16.7+/-1.1
# 113.3+/-0.6
# 0.2+/-0.6
# 3.597+/-0.018
# 0.790+/-0.015