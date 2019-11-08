import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 16

# load data
x, y = np.genfromtxt('Daten.txt', unpack=True)

params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

    x_plot = np.linspace(0, 60)

plt.plot(x, y, 'x', color='b', label="Messwerte")
plt.plot(
    x_plot,
    params[0] * x_plot + params[1],
    label='Lineare Regression',
    linewidth=1,
    color='g'
)
plt.legend(loc="best")

plt.plot(x, y, 'k.', label="Messung der Federauslenkung")
plt.savefig('Plot.pdf')