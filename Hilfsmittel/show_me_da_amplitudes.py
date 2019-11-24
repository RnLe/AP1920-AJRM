import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import math

ID, t1, t2, t3, t4, t5, t6, t7, t8, t = np.genfromtxt("../V204_Waermeleitf/Messung_2(dynamisch).txt", unpack=True)

def getAmplitudes(y, x, which):
    amplitudes = [[], []]
    i = 0
    if which == 'max':
        falling = False
        while i < len(x)-1:
            if y[i] > y[i+1] and not falling:
                amplitudes[0].append(x[i])
                amplitudes[1].append(y[i])
            falling = y[i] > y[i+1] or (y[i] == y[i+1] and falling)
            i += 1
    elif which == 'min':
        falling = False
        while i < len(x)-1:
            if y[i] < y[i+1] and falling:
                amplitudes[0].append(x[i])
                amplitudes[1].append(y[i])
            falling = y[i] > y[i+1] or (y[i] == y[i+1] and falling)
            i += 1

    return amplitudes

maxima_t1 = getAmplitudes(t1, t, 'max')
minima_t1 = getAmplitudes(t1, t, 'min')
maxima_t2 = getAmplitudes(t2, t, 'max')
minima_t2 = getAmplitudes(t2, t, 'min')

def possible_plot(x, a, b, c, d):
    return (d*math.log((x-a), b) + c)

# params, params_covariance = optimize.curve_fit(possible_plot, minima_t1[0], minima_t1[1], p0=[2, 2, 2, 2])

# print(params)
# plt.figure()
# plt.plot(minima_t1[0], possible_plot(minima_t1[0], params[0], params[1], params[2], params[3]))
# plt.show()

print(maxima_t1)
print(minima_t1)