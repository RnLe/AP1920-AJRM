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

#Plot lange Spule
plt.clf()
x=np.array([-79,-74,-69,-64,-59,-48,-40,-32,-24,-15,-9,1,21])
y=np.array([3.076,3.051,3.020,2.977,2.916,2.671,2.318,1.775,1.174,0.680,0.501,0.317,0.177,])

plt.plot(x,y,'c.')
plt.grid()
plt.xlabel(r'$y\,/\,\mathrm{mm}$')
plt.ylabel(r'$B\,/\,\mathrm{mT}$')
plt.savefig('plot_langSp.pdf')

#Plot kurze Spule
plt.clf()
x=np.array([-96,-81,-66,-56,-46,-36,-23,-9,4,14,25,39,55])
y=np.array([13.71,16.68,18.48,18.81,18.44,17.40,15.02,11.82,8.82,6.90,5.23,3.68,2.52])

plt.plot(x,y,'c.')
plt.grid()
plt.xlabel(r'$y\,/\,\mathrm{mm}$')
plt.ylabel(r'$B\,/\,\mathrm{mT}$')
plt.savefig('plot_kurzSp.pdf')