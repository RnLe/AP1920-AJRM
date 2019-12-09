import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams.update({
'font.family': 'serif',
'text.usetex': True,
'pgf.rcfonts': False,
'pgf.texsystem': 'lualatex',
'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}',
})

x=np.array([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,8.0,7.0,6.0,5.0,4.0,3.0,2.0,1.0,0.0,-0.65,-1.0,-2.0,-3.0,-4.0,-5.0,-6.0,-7.0,-8.0,-9.0,-8.0,-7.0,-6.0,-5.0,-4.0,-3.0,-2.0,-1.0,0.0,0.6,0.675,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
y=np.array([0,148,335,440,508,561,603,638,668,698,677,656,632,604,569,524,460,332,128,0,71,252,390,482,546,594,634,669,698,679,658,635,607,573,529,464,339,129,8,0,72,253,390,482,544,592,630,663,693])
y[20:39]=-y[20:39] #Minuszeichen bei Daten erst nicht aufgenommen, hier nachgeholt

#B-Feld der Spule ohne Eisenkern
my_0=4*np.pi*10**(-7)
n=595
r=0.135
#Strom I entspricht den x gespeicherten Werten
H_Faktor=n*(2*np.pi*r)**(-1)
B_Faktor=my_0*n*(2*np.pi*r)**(-1)
H_Spule=H_Faktor*x
B_Magnetisierung=(y*10**(-3)*(my_0)**(-1)-H_Spule)*my_0*10**3 


plt.plot(H_Spule[0:10],B_Magnetisierung[0:10],'b.',label='1. Kurve')
plt.plot(H_Spule[10:29],B_Magnetisierung[10:29],'g.',label='2. Kurve')
plt.plot(H_Spule[30:50],B_Magnetisierung[30:50],'c.',label='3. Kurve')
plt.plot(H_Spule[9:10],B_Magnetisierung[9:10],'r*',label='Sättigung')
plt.plot(H_Spule[18:19],B_Magnetisierung[18:19],'k*',label='Remanenz')
plt.plot(H_Spule[19:20],B_Magnetisierung[19:20],'y*',label='Koerzitivkraft')
plt.plot(H_Spule[28:29],B_Magnetisierung[28:29],'r*') #negative Sättigung
plt.plot(H_Spule[37:38],B_Magnetisierung[37:38],'k*') #negative Remanenz
plt.plot(H_Spule[39:40],B_Magnetisierung[39:40],'y*') #positive Koerzitivkraft

plt.legend()
plt.grid()

plt.xlabel(r'$H\,/\,\si{\ampere\per\meter}$')
plt.ylabel(r'$B\,/\,\mathrm{mT}$')
plt.savefig('plot_Hysterese.pdf')

print(H_Spule)
print(B_Magnetisierung)