#irgendwas mache ich falsch...
#HH1 = Helmholtz 1. Messung

import matplotlib.pyplot as plt
import numpy as np

x=np.array([7,9,10.5,12,13.5,68.5,69,70,75,80,85,90,95,100])
y=np.array([4.239,4.231,4.234,4.260,4.239,3.003,2.960,2.891,2.666,2.445,2.219,2.018,1.839,1.662])
plt.plot(x,y,'ro')
#plt.plot([7,9,10.5,12,13.5,68.5,69,70,75,80,85,90,95,100],[4.239,4.231,4.234,4.260,4.239,3.003,2.960,2.891,2.666,2.445,2.219,2.018,1.839,1.662],'ro')
plt.savefig('plot1.pdf')