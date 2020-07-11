import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.optimize import curve_fit
import cmath
import sys
from mpl_toolkits.mplot3d import Axes3D

# gui_backend ist ein flag, um das backend von mpl von latex zu einem interaktiven gui zu schalten
# pgf unterstützt kein show(). Bei einem 3D Plot ist es sinnvoll, diesen rotieren und aktiv betrachten zu können,
# statt 20 Perspektiven als pdf abzuspeichern, um eine Vorstellung von der Geometrie zu kriegen.
# Um die gui nutzen zu können: diese Datei aus einem Verzeichnis öffnen, in dem header-matplotlib.tex und matplotlibrc NICHT sind.
# zudem -gui hinter die PythonDatei schreiben.
gui_backend = False
if len(sys.argv) != 1 and sys.argv[1] == "-gui":
    gui_backend = True

if (gui_backend): mpl.use('TkAgg')
else:
    mpl.use('pgf')
    mpl.rcParams.update({
    'font.size': 10,
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'pgf.texsystem': 'lualatex',
    'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}',
    })

# y-Achse ist µA und x-Achse mm
# -> daher alle Werte in mm und µA umrechnen
I2 = np.genfromtxt('../data/Messdaten_V406_2.txt', comments='#', unpack=True)
lam = 633*10**-6    # Wellenlänge
_d = 626.1          # Abstand zum Sensor
_b = 0.075          # Spaltbreite
Id = 0.8            # Dunkelstrom
x0 = 11.727         # Intensitätsmaximum

def forReal(x, a, b):
    x_ = abs(x - x0)
    d_ = np.sqrt(_d**2 + x_**2)
    sin_phi = x_ / d_
    eta = (np.pi * b * sin_phi) / lam
    return ((a*np.sinc(eta))**2)*10**6 + Id

# Intervall für die Parameter
# Kleinere Bereiche = Höhere Auflösung
# ---------------------------
amin, amax, bmin, bmax = [0.000001, 1, 0.0001, 1]
# amin, amax, bmin, bmax = [0.00001, 0.01, 0.0001, 1]
# amin, amax, bmin, bmax = [0.00001, 0.006, 0.0001, 0.1]
# amin, amax, bmin, bmax = [0.0015, 0.005, 0.001, 0.08]
# amin, amax, bmin, bmax = [0.0025, 0.0043, 0.02, 0.035]
# ---------------------------
a = np.linspace(amin, amax, 1000)
b = np.linspace(bmin, bmax, 1000)

print('constructing meshgrid..', end =" ", flush=True)
av, bv = np.meshgrid(a, b)
print('done')

print('constructing target matrix..', end =" ", flush=True)
c = [[0 for i in range(len(a))] for j in range(len(b))]
print('done')

print('filling target matrix..', end =" ", flush=True)
for k in range(len(I2[0])):
            c += (I2[1][k] - forReal(I2[0][k], av, bv))**2
print('done')

print('logging..', end =" ", flush=True)
c = np.log10(c)
print('done')

c_min = []
ab = []
n = 190
# Schleife, um die n kleinsten Werte zu extrahieren
for i in range(n):
    # c.argmin() findet den Index des geringsten Wertes für das flattened array
    # np.unravel_index übersetzt den Index der flattened array für ein array der angegebenen Form (c.shape)
    ab.append(np.unravel_index(c.argmin(), c.shape))
    # Parameterwerte der entsprechenden Indexe
    a_min = a[ab[i][1]]
    b_min = b[ab[i][0]]

    # Werte notieren
    c_min.append([a_min, b_min, c[ab[i]]])
    # Minimum entfernen
    c[ab[i]] = float('inf')

# Werte für a um 10³ erhöhen, um die Achsenbeschriftung lesbarer zu machen
# av *= 10**3

# nach a sortieren
c_min = sorted(c_min, key=lambda x:x[0])

# extrahierte Minima wieder in das Array eintragen
for i in range(n):
    c[ab[i]] = c_min[i][2]


# for i in range(len(c_min)):
#     print(c_min[i])

# Liste transponieren
c_min = list(map(list, zip(*c_min)))

# Vertikale Ebene
cl = np.linspace(-1, 1, 10)
ap, cp = np.meshgrid(a, cl)
bp = np.array([[0.075 for i in range(len(a))] for j in range(len(cl))])



# ------------------------ Vorbereitung auf das Plotten verschiedener a Werte --------------------
# Liste in drei Teile teilen
tempIndex1 = c_min[0].index(0.0030039999999999997)
c_min1 = [c_min[1][:tempIndex1], c_min[2][:tempIndex1]]
tempIndex2 = c_min[0].index(0.004005)
c_min2 = [c_min[1][tempIndex1:tempIndex2], c_min[2][tempIndex1:tempIndex2]]
c_min3 = [c_min[1][tempIndex2:], c_min[2][tempIndex2:]]

print('plotting..', end =" ", flush=True)
plt.plot(*c_min1, 'b.')
plt.plot(*c_min2, 'g.')
plt.plot(*c_min3, 'r.')
plt.xlabel(r'b\:/\:mm')
plt.ylabel(r'log(c)\:/\:$\mu A^2$')
plt.legend([r'$a \approx 0.002$', r'$a \approx 0.003$', r'$a \approx 0.004$'])
plt.savefig('2DPlot')
print('done')
# plt.close()
# -------------------------------------------------------------------------------------------------


# -----------------------------------------------
# print('plotting..', end =" ", flush=True)
# fig = plt.figure()
# ax = fig.gca(projection='3d', azim=140, elev=20) # azim=140 für leastSquared5.pdf, 160 sonst

# surf = ax.plot_surface(av, bv, c, cmap=mpl.cm.magma, rcount=100, ccount=100, antialiased=False)
# # plane = ax.plot_surface(ap, bp, cp, label='Reale Spaltbreite', color='grey')
# # bug von matplotlib: label für surface-plots müssen mit den nächsten Zeilen vorbereitet werden
# surf._facecolors2d=surf._facecolors3d
# surf._edgecolors2d=surf._edgecolors3d
# # plane._facecolors2d=plane._facecolors3d
# # plane._edgecolors2d=plane._edgecolors3d
# # bug Ende
# # ax.legend()
# ax.tick_params(labelsize=7)
# ax.set_xlabel(r'$a$\:/\:$\sqrt{\mu A}$')
# ax.set_ylabel(r'b\:/\:mm')
# ax.set_zlabel(r'log(c)\:/\:$\mu A^2$')
# fig.colorbar(surf, shrink=0.5, pad=0.09)

# # plt.savefig('leastSquares.pdf')
# # plt.savefig('leastSquares2.pdf')
# # plt.savefig('leastSquares3.pdf')
# # plt.savefig('leastSquares4.pdf')
# plt.savefig('leastSquares5.pdf')
# # plt.show()
# print('done')