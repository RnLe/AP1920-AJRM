import matplotlib.pyplot as plt
import numpy as np

ID, t1, t2, t3, t4, t5, t6, t7, t8, t = np.genfromtxt("Messung_1(statisch).txt", unpack=True)

# plotting of the far temperatures as pairs; t1, t4 and t5, t8
fig1, ax1 = plt.subplots()
ax1.plot(t, t1, color='#F5C400')
ax1.plot(t, t4, 'y')
ax1.set_xlabel(r'Zeit $t / \si{\second}$')
ax1.set_ylabel(r'Temperatur $T / \si{\celsius}$')
ax1.legend(['Messing(b)', 'Messing(s)'])

fig2, ax2 = plt.subplots()
ax2.plot(t, t5, color='#98bfe3')
ax2.plot(t, t8, color='#737373')
ax2.set_xlabel(r'Zeit $t / \si{\second}$')
ax2.set_ylabel(r'Temperatur $T / \si{\celsius}$')
ax2.legend(['Aluminium', 'Edelstahl'])

fig3, ax3 = plt.subplots()
ax3.plot(t, t7-t8)
ax3.set_xlabel(r'Zeit $t / \si{\second}$')
ax3.set_ylabel('$Temperaturdifferenz_T7-T8$')

fig4, ax4 = plt.subplots()
ax4.plot(t, t2-t1)
ax4.set_xlabel(r'Zeit $t / \si{\second}$')
ax4.set_ylabel('$Temperaturdifferenz_T2-T1$')

ID, t1, t2, t3, t4, t5, t6, t7, t8, t = np.genfromtxt("Messung_2(dynamisch).txt", unpack=True)
fig5, ax5 = plt.subplots()
for y in (t1, t2, t3, t4, t5, t6, t7, t8):
    ax5.plot(t, y)
ax5.set_xlabel(r'Zeit $t / \si{\second}$')
ax5.set_ylabel(r'Temperatur $T / \si{\celsius}$')

ID, t1, t2, t3, t4, t5, t6, t7, t8, t = np.genfromtxt("Messung_3(dynamisch).txt", unpack=True)
fig6, ax6 = plt.subplots()
for y in (t1, t2, t3, t4, t5, t6, t7, t8):
    ax6.plot(t, y)
ax6.set_xlabel(r'Zeit $t / \si{\second}$')
ax6.set_ylabel(r'Temperatur $T / \si{\celsius}$')

fig1.savefig('build/plot_t1_t4.pdf')
fig2.savefig('build/plot_t5_t8.pdf')
fig3.savefig('build/plot_tempDiff_t7t8.pdf')
fig4.savefig('build/plot_tempDiff_t2t1.pdf')
fig5.savefig('build/plot2.pdf')
fig6.savefig('build/plot3.pdf')