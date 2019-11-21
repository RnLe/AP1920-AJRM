import matplotlib.pyplot as plt
import numpy as np

ID, t1, t2, t3, t4, t5, t6, t7, t8, t = np.genfromtxt("Messung_1(statisch).txt", unpack=True)

fig1, ax1 = plt.subplots()
for y in (t1, t2, t3, t4, t5, t6, t7, t8):
    ax1.plot(t, y)
ax1.set_xlabel(r'Zeit $t / \si{\second}$')
ax1.set_ylabel(r'Temperatur $T / si{\celsius}$')

ID, t1, t2, t3, t4, t5, t6, t7, t8, t = np.genfromtxt("Messung_2(dynamisch).txt", unpack=True)
fig2, ax2 = plt.subplots()
for y in (t1, t2, t3, t4, t5, t6, t7, t8):
    ax2.plot(t, y)
ax2.set_xlabel('$Zeit_s$')
ax2.set_ylabel('$Temperatur_°C$')

ID, t1, t2, t3, t4, t5, t6, t7, t8, t = np.genfromtxt("Messung_3(dynamisch).txt", unpack=True)
fig3, ax3 = plt.subplots()
for y in (t1, t2, t3, t4, t5, t6, t7, t8):
    ax3.plot(t, y)
ax3.set_xlabel('$Zeit_s$')
ax3.set_ylabel('$Temperatur_°C$')

fig1.savefig('build/plot1.pdf')
fig2.savefig('build/plot2.pdf')
fig3.savefig('build/plot3.pdf')