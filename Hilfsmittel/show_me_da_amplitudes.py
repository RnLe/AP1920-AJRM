import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# depending on the folder you're in (1. /Hilfsmittel, 2. /V204_Waermeleitf)
ID, t1, t2, t3, t4, t5, t6, t7, t8, t = np.genfromtxt("../V204_Waermeleitf/data/Messung_2(dynamisch).txt", unpack=True)
# ID, t1, t2, t3, t4, t5, t6, t7, t8, t = np.genfromtxt("../data/Messung_2(dynamisch).txt", unpack=True)
count = 1

# function to extract the amplitudes of a sine-like function
def getAmplitudes(y, x, AType):
    amplitudes = [[], []]
    i = 0
    if AType == 'max':
        falling = False
        while i < len(x)-1:
            if y[i] > y[i+1] and not falling:
                amplitudes[0].append(x[i])
                amplitudes[1].append(y[i])
            falling = y[i] > y[i+1] or (y[i] == y[i+1] and falling)
            i += 1
    elif AType == 'min':
        falling = False
        while i < len(x)-1:
            if y[i] < y[i+1] and falling:
                amplitudes[0].append(x[i])
                amplitudes[1].append(y[i])
            falling = y[i] > y[i+1] or (y[i] == y[i+1] and falling)
            i += 1

    return amplitudes

def plot_and_write(x_values, y_values, material, function):
    # create evenly spaced x values in the given range for maximized accuracy
    global count
    x_even = np.linspace(t[1], t[len(t)-1], 1000)

    # ---------------------------
    # curve fitting, amplitudes, Δt

    # get the amplitudes
    maxima = getAmplitudes(y_values, x_values, 'max')
    minima = getAmplitudes(y_values, x_values, 'min')

    x = minima[0]
    y = minima[1]

    # curve fit!
    params, params_covariance = optimize.curve_fit(function, x, y, p0=[0, 1, 1])

    # plot everything you need
    fig = plt.figure(count)
    plt.plot(x_even, function(x_even, params[0], params[1], params[2]))
    plt.plot(x, y, 'r+')
    plt.plot(x_values, y_values)
    plt.plot(maxima[0], maxima[1], 'g+')
    for i in range(len(maxima[0])):
        plt.plot((maxima[0][i], maxima[0][i]), (log_like_func(maxima[0][i], params[0], params[1], params[2]), maxima[1][i]), color='k')
    plt.legend(['Ausgleichskurve Minima', 'Minima', 'Messkurve', 'Maxima', 'Amplituden'])
    plt.title(material)
    plt.savefig(f'amplitudes_{material}.pdf')
    fig.show()

    # write the data to a file
    with open(f'amplitudes_{material}.txt', 'w') as f:
        f.write(f"Parameters for c*ln(x-a)+b = {params}\n\n")
        f.write(f"Minima for {material}\n")
        f.write("t\t\t°C\n")
        for i in range(len(minima[0])):
            f.write(f"{minima[0][i]}\t\t{minima[1][i]}\n")
        f.write(f"\nMaxima for {material}\n")
        f.write("t\t\t°C\n")
        for i in range(len(maxima[0])):
            f.write(f"{maxima[0][i]}\t\t{maxima[1][i]}\n")
        f.write("\nphase difference Δt\n")
        f.write("maxima\tminima\t\tΔt\n")
        # important!: there are less minima than maxima
        for i in range(len(minima[0])):
            f.write(f"{maxima[0][i]}\t{minima[0][i]}\t\t{round(abs(minima[1][i]-maxima[1][i]), 4)}\n")
    
    count += 1

# in this case the minima/maxima lie on a log-like function
def log_like_func(x, a, b, c):
    return (c*np.log(x-a) + b)

plot_and_write(t, t1, "brass_wide_far(t1)", log_like_func)
plot_and_write(t, t2, "brass_wide_close(t2)", log_like_func)
plot_and_write(t, t5, "aluminum_far(t5)", log_like_func)
plot_and_write(t, t6, "aluminum_close(t6)", log_like_func)
plot_and_write(t, t7, "steel_close(t7)", log_like_func)

# without input() the plots won't be shown
# input()

#doesn't work 'cause there are no extrema, just turning points
#plot_and_write(t, t8, "steel_far(t8)", log_like_func)


# # brass
# # far

# # close
# maxima_t2 = getAmplitudes(t2, t, 'max')
# minima_t2 = getAmplitudes(t2, t, 'min')

# # aluminum
# # far
# maxima_t5 = getAmplitudes(t5, t, 'max')
# minima_t5 = getAmplitudes(t5, t, 'min')
# # close
# maxima_t6 = getAmplitudes(t6, t, 'max')
# minima_t6 = getAmplitudes(t6, t, 'min')

# # steel
# # close
# maxima_t7 = getAmplitudes(t7, t, 'max')
# minima_t7 = getAmplitudes(t7, t, 'min')
# # far
# maxima_t8 = getAmplitudes(t8, t, 'max')
# minima_t8 = getAmplitudes(t8, t, 'min')

# # the above function isn't perfect. check values for plausibility and delete (pop) those values
# # e.g. minima_t1's first value is invalid
# minima_t1[0].pop(0)
# minima_t1[1].pop(0)
# maxima_t1[0].pop(1)
# maxima_t1[1].pop(1)





# # ---------------------------
# # curve fitting, amplitudes, Δt for t2
# material = "brass_wide_close(t2)"

# x = minima_t2[0]
# y = minima_t2[1]

# # curve fit!
# params_t2, params_t2_covariance = optimize.curve_fit(log_like_func, x, y, p0=[0, 1, 1])

# # plot everything you need
# g = plt.figure(2)
# plt.plot(x_even, log_like_func(x_even, params_t2[0], params_t2[1], params_t2[2]))
# plt.plot(x, y, 'r+')
# plt.plot(t, t2)
# plt.plot(maxima_t2[0], maxima_t2[1], 'g+')
# for i in range(len(maxima_t2[0])):
#     plt.plot((maxima_t2[0][i], maxima_t2[0][i]), (log_like_func(maxima_t2[0][i], params_t2[0], params_t2[1], params_t2[2]), maxima_t2[1][i]), color='k')
# plt.legend(['Ausgleichskurve Minima', 'Minima', 'Messkurve', 'Maxima', 'Amplituden'])
# plt.savefig(f'amplitudes_{material}.pdf')
# g.show()


# # write the data to a file
# with open(f'amplitudes_{material}.txt', 'w') as f:
#     f.write(f"Parameters for c*ln(x-a)+b = {params_t2}\n\n")
#     f.write(f"Minima for {material}\n")
#     f.write("t\t\t°C\n")
#     for i in range(len(minima_t2[0])):
#         f.write(f"{minima_t2[0][i]}\t\t{minima_t2[1][i]}\n")
#     f.write(f"\nMaxima for {material}\n")
#     f.write("t\t\t°C\n")
#     for i in range(len(maxima_t2[0])):
#         f.write(f"{maxima_t2[0][i]}\t\t{maxima_t2[1][i]}\n")
#     f.write("\nphase difference Δt\n")
#     f.write("maxima\tminima\t\tΔt\n")
#     # important!: there are less minima than maxima
#     for i in range(len(minima_t2[0])):
#         f.write(f"{maxima_t2[0][i]}\t{minima_t2[0][i]}\t\t{round(abs(minima_t2[1][i]-maxima_t2[1][i]), 4)}\n")

# # ---------------------------
# # curve fitting, amplitudes, Δt for t5
# material = "aluminum_far(t5)"

# x = minima_t5[0]
# y = minima_t5[1]

# # curve fit!
# params_t5, params_t5_covariance = optimize.curve_fit(log_like_func, x, y, p0=[0, 1, 1])

# # plot everything you need
# h = plt.figure(3)
# plt.plot(x_even, log_like_func(x_even, params_t5[0], params_t5[1], params_t5[2]))
# plt.plot(x, y, 'r+')
# plt.plot(t, t5)
# plt.plot(maxima_t5[0], maxima_t5[1], 'g+')
# for i in range(len(maxima_t5[0])):
#     plt.plot((maxima_t5[0][i], maxima_t5[0][i]), (log_like_func(maxima_t5[0][i], params_t5[0], params_t5[1], params_t5[2]), maxima_t5[1][i]), color='k')
# plt.legend(['Ausgleichskurve Minima', 'Minima', 'Messkurve', 'Maxima', 'Amplituden'])
# plt.savefig(f'amplitudes_{material}.pdf')
# h.show()

# # write the data to a file
# with open(f'amplitudes_{material}.txt', 'w') as f:
#     f.write(f"Parameters for c*ln(x-a)+b = {params_t5}\n\n")
#     f.write(f"Minima for {material}\n")
#     f.write("t\t\t°C\n")
#     for i in range(len(minima_t5[0])):
#         f.write(f"{minima_t5[0][i]}\t\t{minima_t5[1][i]}\n")
#     f.write(f"\nMaxima for {material}\n")
#     f.write("t\t\t°C\n")
#     for i in range(len(maxima_t5[0])):
#         f.write(f"{maxima_t5[0][i]}\t\t{maxima_t5[1][i]}\n")
#     f.write("\nphase difference Δt\n")
#     f.write("maxima\tminima\t\tΔt\n")
#     # important!: there are less minima than maxima
#     for i in range(len(minima_t5[0])):
#         f.write(f"{maxima_t5[0][i]}\t{minima_t5[0][i]}\t\t{round(abs(minima_t5[1][i]-maxima_t5[1][i]), 4)}\n")

# # ---------------------------
# # curve fitting, amplitudes, Δt for t6
# material = "aluminum_close(t6)"

# x = minima_t6[0]
# y = minima_t6[1]

# # curve fit!
# params_t6, params_t6_covariance = optimize.curve_fit(log_like_func, x, y, p0=[0, 1, 1])

# # plot everything you need
# j = plt.figure(4)
# plt.plot(x_even, log_like_func(x_even, params_t6[0], params_t6[1], params_t6[2]))
# plt.plot(x, y, 'r+')
# plt.plot(t, t6)
# plt.plot(maxima_t6[0], maxima_t6[1], 'g+')
# for i in range(len(maxima_t6[0])):
#     plt.plot((maxima_t6[0][i], maxima_t6[0][i]), (log_like_func(maxima_t6[0][i], params_t6[0], params_t6[1], params_t6[2]), maxima_t6[1][i]), color='k')
# plt.legend(['Ausgleichskurve Minima', 'Minima', 'Messkurve', 'Maxima', 'Amplituden'])
# plt.savefig(f'amplitudes_{material}.pdf')
# j.show()

# # write the data to a file
# with open(f'amplitudes_{material}.txt', 'w') as f:
#     f.write(f"Parameters for c*ln(x-a)+b = {params_t6}\n\n")
#     f.write(f"Minima for {material}\n")
#     f.write("t\t\t°C\n")
#     for i in range(len(minima_t6[0])):
#         f.write(f"{minima_t6[0][i]}\t\t{minima_t6[1][i]}\n")
#     f.write(f"\nMaxima for {material}\n")
#     f.write("t\t\t°C\n")
#     for i in range(len(maxima_t6[0])):
#         f.write(f"{maxima_t6[0][i]}\t\t{maxima_t6[1][i]}\n")
#     f.write("\nphase difference Δt\n")
#     f.write("maxima\tminima\t\tΔt\n")
#     # important!: there are less minima than maxima
#     for i in range(len(minima_t6[0])):
#         f.write(f"{maxima_t6[0][i]}\t{minima_t6[0][i]}\t\t{round(abs(minima_t6[1][i]-maxima_t6[1][i]), 4)}\n")

# # ---------------------------
# # curve fitting, amplitudes, Δt for t7
# material = "steel_close(t7)"

# x = minima_t7[0]
# y = minima_t7[1]

# # curve fit!
# params_t7, params_t7_covariance = optimize.curve_fit(log_like_func, x, y, p0=[0, 1, 1])

# # plot everything you need
# k = plt.figure(5)
# plt.plot(x_even, log_like_func(x_even, params_t7[0], params_t7[1], params_t7[2]))
# plt.plot(x, y, 'r+')
# plt.plot(t, t7)
# plt.plot(maxima_t7[0], maxima_t7[1], 'g+')
# for i in range(len(maxima_t7[0])):
#     plt.plot((maxima_t7[0][i], maxima_t7[0][i]), (log_like_func(maxima_t7[0][i], params_t7[0], params_t7[1], params_t7[2]), maxima_t7[1][i]), color='k')
# plt.legend(['Ausgleichskurve Minima', 'Minima', 'Messkurve', 'Maxima', 'Amplituden'])
# plt.savefig(f'amplitudes_{material}.pdf')
# k.show()

# # write the data to a file
# with open(f'amplitudes_{material}.txt', 'w') as f:
#     f.write(f"Parameters for c*ln(x-a)+b = {params_t7}\n\n")
#     f.write(f"Minima for {material}\n")
#     f.write("t\t\t°C\n")
#     for i in range(len(minima_t7[0])):
#         f.write(f"{minima_t7[0][i]}\t\t{minima_t7[1][i]}\n")
#     f.write(f"\nMaxima for {material}\n")
#     f.write("t\t\t°C\n")
#     for i in range(len(maxima_t7[0])):
#         f.write(f"{maxima_t7[0][i]}\t\t{maxima_t7[1][i]}\n")
#     f.write("\nphase difference Δt\n")
#     f.write("maxima\tminima\t\tΔt\n")
#     # important!: there are less minima than maxima
#     for i in range(len(minima_t7[0])):
#         f.write(f"{maxima_t7[0][i]}\t{minima_t7[0][i]}\t\t{round(abs(minima_t7[1][i]-maxima_t7[1][i]), 4)}\n")

# ---------------------------
# curve fitting, amplitudes, Δt for t8
# doesn't work 'cause there are no extrema, just turning points

# material = "steel_far(t8)"

# x = minima_t8[0]
# y = minima_t8[1]

# # curve fit!
# params_t8, params_t8_covariance = optimize.curve_fit(log_like_func, x, y, p0=[0, 1, 1])

# # plot everything you need
# l = plt.figure(6)
# plt.plot(x_even, log_like_func(x_even, params_t8[0], params_t8[1], params_t8[2]))
# plt.plot(x, y, 'r+')
# plt.plot(t, t8)
# plt.plot(maxima_t8[0], maxima_t8[1], 'g+')
# for i in range(len(maxima_t8[0])):
#     plt.plot((maxima_t8[0][i], maxima_t8[0][i]), (log_like_func(maxima_t8[0][i], params_t8[0], params_t8[1], params_t8[2]), maxima_t8[1][i]), color='k')
# plt.legend(['Ausgleichskurve Minima', 'Minima', 'Messkurve', 'Maxima', 'Amplituden'])
# plt.savefig(f'amplitudes_{material}.pdf')
# l.show()

# # write the data to a file
# with open(f'amplitudes_{material}.txt', 'w') as f:
#     f.write(f"Parameters for c*ln(x-a)+b = {params_t8}\n\n")
#     f.write(f"Minima for {material}\n")
#     f.write("t\t\t°C\n")
#     for i in range(len(minima_t8[0])):
#         f.write(f"{minima_t8[0][i]}\t\t{minima_t8[1][i]}\n")
#     f.write(f"\nMaxima for {material}\n")
#     f.write("t\t\t°C\n")
#     for i in range(len(maxima_t8[0])):
#         f.write(f"{maxima_t8[0][i]}\t\t{maxima_t8[1][i]}\n")
#     f.write("\nphase difference Δt\n")
#     f.write("maxima\tminima\t\tΔt\n")
#     # important!: there are less minima than maxima
#     for i in range(len(minima_t8[0])):
#         f.write(f"{maxima_t8[0][i]}\t{minima_t8[0][i]}\t\t{round(abs(minima_t8[1][i]-maxima_t8[1][i]), 4)}\n")