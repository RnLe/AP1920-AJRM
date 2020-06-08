import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat

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

x_plot=np.linspace(-1,5)

plt.subplot(2,1,1)
plt.plot(x_plot,np.sin(x_plot),'b-',label='Generator')
plt.plot(x_plot,-np.cos(x_plot),'m-',label='Integral')
plt.xlim(-1,5)
#plt.axis('off')
plt.legend()
plt.title('Sinusspannung')

plt.subplot(2,1,2)
for i in np.arange(3):
    x_n=np.linspace(-1+2*i,2*i+1)
    plt.plot(x_n,(-1)**i*np.ones(50),'b-')#,label='Generator')
    plt.plot(x_n,(-1)**i *(x_n-2*i),'m-')#,label='Integral')
plt.xlim(-1,5)
plt.axvline(x=1,ymin=0.046, ymax=0.954,color='b')
plt.axvline(x=3,ymin=0.046, ymax=0.954,color='b')
#plt.axis('off')
#plt.legend()
plt.title('Rechteckspannung')

plt.savefig('erwart_int1.pdf')

#plt.subplot(3,1,3)
plt.clf()
for i in np.arange(3):
    x_k=np.linspace(-1+2*i,2*i+1)
    plt.plot(x_k,0.5-abs(x_k-2*i),'b-')#,label='Generator')
    plt.plot(x_k,(0.5*(x_k-2*i)-0.5*(x_k-2*i)*abs(x_k-2*i))*4,'m-')#,label='Integral')
plt.xlim(-1,5)
#plt.axis('off')
#plt.legend()
plt.title('Dreieckspannung')

#plt.tight_layout()

plt.savefig('erwart_int2.pdf')
