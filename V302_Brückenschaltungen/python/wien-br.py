import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
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


f=np.array([213.0,263.0,313.0,363.0,413.0,463.0,513.0,563.0,573.0,583.0,593.0,603.0,613.0,623.0,633.0,643.0,653.0,663.0,713.0,763.0,813.0,863.0,913.0,963.0,1013.0])
f_f_0=f/613.0
U_BR=np.array([ 460,360,290,230,175,122,80,38,32,24,16,10,6,10,20,30,36,40,67,95,125,148,170,190,215])
U_BR_rel=U_BR/4000

print('f/f0:')
print(f_f_0)
print('U_br/U_S')
print(U_BR_rel)

#Messwerte wie gefordert plotten:
plt.plot(f_f_0,U_BR_rel,'r.',label='Messwerte') 
plt.yscale('log')
plt.xlabel(r'$\Omega$')
plt.ylabel(r'$U_\text{Br}\,/\,U_\text{Sp}$')
plt.grid()

x = np.linspace(0.25, 1.75)
plt.plot(x,(1/3)*abs(x**2 -1)/((x**2 -1)**2 + 9*x**2)**(1/2),label='Berechnete Kurve')

plt.legend()
plt.savefig('plot_wien.pdf')


# f/f0:
# [0.34747145 
#  0.42903752 
#  0.51060359 
#  0.59216966 
#  0.67373573 
#  0.75530179
#  0.83686786 
#  0.91843393 
#  0.93474715 
#  0.95106036 
#  0.96737357 
#  0.98368679
#  1.         
#  1.01631321 
#  1.03262643 
#  1.04893964 
#  1.06525285 
#  1.08156607
#  1.16313214 
#  1.24469821 
#  1.32626427 
#  1.40783034 
#  1.48939641 
#  1.57096248
#  1.65252855]
# U_br/U_S
# [0.115   
#  0.09    
#  0.0725  
#  0.0575  
#  0.04375 
#  0.0305  
#  0.02    
#  0.0095  
#  0.008
#  0.006   
#  0.004   
#  0.0025  
#  0.0015  
#  0.0025  
#  0.005   
#  0.0075  
#  0.009   
#  0.01
#  0.01675 
#  0.02375 
#  0.03125 
#  0.037   
#  0.0425  
#  0.0475  
#  0.05375]
#  
