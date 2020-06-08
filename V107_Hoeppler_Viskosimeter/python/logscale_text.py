import numpy as np
import matplotlib.pyplot as plt

# import matplotlib as mpl
# mpl.use('pgf')
# import matplotlib.pyplot as plt
# mpl.rcParams.update({
# 'font.family': 'serif',
# 'text.usetex': True,
# 'pgf.rcfonts': False,
# 'pgf.texsystem': 'lualatex',
# 'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}',
# })

def func(x, a, b):
    return a*x**b

def func_lin(x, a, b):
    return np.log(a) + b*np.log(x)

x_vals = np.linspace(0, 10, 200)

plt.plot(x_vals, func(x_vals, 1, -1))
plt.plot(np.log(x_vals), func_lin(x_vals, 1, -1))
plt.show()