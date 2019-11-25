import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import sys
import math
from uncertainties import ufloat, umath
import uncertainties.unumpy as unp

make_string = "../"
if len(sys.argv) != 1 and sys.argv[1] == "-up":
    make_string = ""

# depending on the folder you're in (1. /Hilfsmittel, 2. /V204_Waermeleitf)
# ID, t1, t2, t3, t4, t5, t6, t7, t8, t = np.genfromtxt("../V204_Waermeleitf/Messung_2(dynamisch).txt", unpack=True)
ID, t1, t2, t3, t4, t5, t6, t7, t8, t = np.genfromtxt(f"{make_string}data/Messung_2(dynamisch).txt", unpack=True)
ID_, t1_, t2_, t3_, t4_, t5_, t6_, t7_, t8_, t_ = np.genfromtxt(f"{make_string}data/Messung_3(dynamisch).txt", unpack=True)
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
    x_even = np.linspace(x_values[1], x_values[len(x_values)-1], 1000)

    # ---------------------------
    # curve fitting, amplitudes, Δt

    # get the amplitudes
    maxima = getAmplitudes(y_values, x_values, 'max')
    minima = getAmplitudes(y_values, x_values, 'min')

    if material == "steel_far(t8)":
        minima[0].pop(0)
        minima[1].pop(0)
        minima[0].pop(0)
        minima[1].pop(0)
        minima[0].pop(5)
        minima[1].pop(5)
        maxima[0].pop(0)
        maxima[1].pop(0)
        maxima[0].pop(0)
        maxima[1].pop(0)
        maxima[0].pop(6)
        maxima[1].pop(6)
    if material == "steel_close(t7)":
        minima[0].pop(0)
        minima[1].pop(0)
        maxima[0].pop(0)
        maxima[1].pop(0)
    if material == "brass_wide_far(t1)":
        minima[0].pop(0)
        minima[1].pop(0)
        maxima[0].pop(0)
        maxima[1].pop(0)

    x = minima[0]
    y = minima[1]

    # curve fit!
    params, params_covariance = optimize.curve_fit(function, x, y, p0=[0, 1, 1])

    # plot everything you need
    fig = plt.figure(count)
    plt.plot(x_even, function(x_even, params[0], params[1], params[2]))
    plt.plot(x, y, 'r+')
    plt.xlabel('Zeit')
    plt.ylabel('Temperatur')
    plt.plot(x_values, y_values)
    plt.plot(maxima[0], maxima[1], 'g+')
    for i in range(len(maxima[0])):
        plt.plot((maxima[0][i], maxima[0][i]), (log_like_func(maxima[0][i], params[0], params[1], params[2]), maxima[1][i]), color='k')
    plt.legend(['Ausgleichskurve', 'Minima', 'Messkurve', 'Maxima', 'Amplituden'])
    plt.savefig(f'{make_string}plots/amplitudes_{material}.pdf')
    print(f'amplitudes_{material}.pdf created.')
    fig.show()

    # write the data to a file
    with open(f'{make_string}data/amplitudes_{material}.txt', 'w') as f:
        f.write(f"Parameters for c*ln(x-a)+b = {params}\n\n")
        f.write(f"Minima for {material}\n")
        f.write("t\t\t°C\n")
        for i in range(len(minima[0])):
            f.write(f"{minima[0][i]}\t\t{minima[1][i]}\n")
        f.write(f"\nMaxima for {material}\n")
        f.write("t\t\t°C\n")
        for i in range(len(maxima[0])):
            f.write(f"{maxima[0][i]}\t\t{maxima[1][i]}\n")
    print('amplitudes_{material}.txt created.')  

    # standard deviation
    # ------------------
    sum_ = 0
    for i in range(len(x)):
        sum_ += (y[i] - log_like_func(x[i], *params))**2
    variance_min = math.sqrt(sum_/len(x))


    x = maxima[0]
    y = maxima[1]

    # curve fit!
    params_max, params_max_covariance = optimize.curve_fit(function, x, y, p0=[0, 1, 1])

    sum_ = 0
    for i in range(len(x)):
        sum_ += (y[i] - log_like_func(x[i], *params_max))**2
    variance_max = math.sqrt(sum_/len(x))

    log_min = []
    log_max = []
    for i in range(len(x)):
        log_min.append(log_like_func(maxima[0][i], *params))
        log_max.append(log_like_func(maxima[0][i], *params_max))

    ulog_min = unp.uarray(log_min, variance_min)
    ulog_max = unp.uarray(log_max, variance_max)

    uamps = []
    for i in range(len(ulog_min)):
        uamps.append(ulog_max[i] - ulog_min[i])
    count += 1
    return minima, maxima, uamps, variance_min, variance_max

# in this case the minima/maxima lie on a log-like function
def log_like_func(x, a, b, c):
    return (c*np.log(x-a) + b)

minima_1, maxima_1, amps_1, variance_min_1, variance_max_1 = plot_and_write(t, t1, "brass_wide_far(t1)", log_like_func)
minima_2, maxima_2, amps_2, variance_min_2, variance_max_2 = plot_and_write(t, t2, "brass_wide_close(t2)", log_like_func)
minima_5, maxima_5, amps_5, variance_min_5, variance_max_5 = plot_and_write(t, t5, "aluminum_far(t5)", log_like_func)
minima_6, maxima_6, amps_6, variance_min_6, variance_max_6 = plot_and_write(t, t6, "aluminum_close(t6)", log_like_func)
minima_7, maxima_7, amps_7, variance_min_7, variance_max_7 = plot_and_write(t_, t7_, "steel_close(t7)", log_like_func)
minima_8, maxima_8, amps_8, variance_min_8, variance_max_8 = plot_and_write(t_, t8_, "steel_far(t8)", log_like_func)

    
density = dict(brass=8600, aluminum=2700, steel=7840)
specific_heat_capacity = dict(brass=375, aluminum=920, steel=460)
delta_x = 0.03

# thermal conductivity
# brass
thermal_conductivity_brass = []
numerator = density["brass"]*specific_heat_capacity["brass"]*(delta_x)**2
for i in range(len(amps_1)):
    thermal_conductivity_brass.append(numerator/(2*umath.log(amps_2[i]/amps_1[i])*(maxima_1[0][i]-maxima_2[0][i])))

# mean value of the thermal conductivity
mean_brass = unp.nominal_values(thermal_conductivity_brass).sum()/len(thermal_conductivity_brass)
sum_ = 0
for i in range(len(thermal_conductivity_brass)):
    sum_ += (thermal_conductivity_brass[i] - mean_brass)**2
variance_thermal_con_brass = umath.sqrt(sum_/len(thermal_conductivity_brass))

uthermal_conductivity_brass = ufloat(unp.nominal_values(mean_brass), unp.nominal_values(variance_thermal_con_brass))

# aluminum
thermal_conductivity_aluminum = []
numerator = density["aluminum"]*specific_heat_capacity["aluminum"]*(delta_x)**2
for i in range(len(amps_5)):
    thermal_conductivity_aluminum.append(numerator/(2*umath.log(amps_6[i]/amps_5[i])*(maxima_5[0][i]-maxima_6[0][i])))

# mean value of the thermal conductivity
mean_aluminum = unp.nominal_values(thermal_conductivity_aluminum).sum()/len(thermal_conductivity_aluminum)
sum_ = 0
for i in range(len(thermal_conductivity_aluminum)):
    sum_ += (thermal_conductivity_aluminum[i] - mean_aluminum)**2
variance_thermal_con_aluminum = umath.sqrt(sum_/len(thermal_conductivity_aluminum))

uthermal_conductivity_aluminum = ufloat(unp.nominal_values(mean_aluminum), unp.nominal_values(variance_thermal_con_aluminum))

# steel
thermal_conductivity_steel = []
numerator = density["steel"]*specific_heat_capacity["steel"]*(delta_x)**2
for i in range(len(amps_8)):
    thermal_conductivity_steel.append(numerator/(2*umath.log(amps_7[i]/amps_8[i])*(maxima_8[0][i]-maxima_7[0][i])))

# mean value of the thermal conductivity
mean_steel = unp.nominal_values(thermal_conductivity_steel).sum()/len(thermal_conductivity_steel)
sum_ = 0
for i in range(len(thermal_conductivity_steel)):
    sum_ += (thermal_conductivity_steel[i] - mean_steel)**2
variance_thermal_con_steel = umath.sqrt(sum_/len(thermal_conductivity_steel))

uthermal_conductivity_steel = ufloat(unp.nominal_values(mean_steel), unp.nominal_values(variance_thermal_con_steel))

# WRITE DATA TO FILE
# --------------------------------------
# get the phase difference and amplitude
# brass
with open(f'{make_string}data/phase_amps_tc_variances_brass_wide.txt', 'w') as f:
    f.write("phase difference Δt\n")
    f.write("maxima_close\tmaxima_far\tΔt\n")
    for i in range(len(maxima_1[0])):
        f.write(f"{maxima_2[0][i]}\t\t{maxima_1[0][i]}\t\t{abs(round(maxima_1[0][i]-maxima_2[0][i],4))}\n")
    f.write("\n\tvariance minima\t\tvariance maxima\n")
    f.write(f"FAR\t{variance_min_1}\t{variance_max_1}\n")
    f.write(f"CLOSE\t{variance_min_2}\t{variance_max_2}\n")
    f.write("\namplitudes in Kelvin (from fitted e-function to peak)\n")
    f.write("brass wide FAR (A1_brass)\n")
    f.write("t\tΔT (amplitude)\n")
    for i in range(len(amps_1)):
        f.write(f"{maxima_1[0][i]}\t{amps_1[i]}\t\n")
    f.write("\nbrass wide CLOSE (A2_brass)\n")
    f.write("t\tΔT (amplitude)\n")
    for i in range(len(amps_2)):
        f.write(f"{maxima_2[0][i]}\t{amps_2[i]}\t\n")
    f.write(f"\nthermal conductivity brass = {uthermal_conductivity_brass}\n")
    

# aluminum
with open(f'{make_string}data/phase_amps_tc_variances_aluminum.txt', 'w') as f:
    f.write("phase difference Δt\n")
    f.write("maxima_close\tmaxima_far\tΔt\n")
    for i in range(len(maxima_5[0])):
        f.write(f"{maxima_6[0][i]}\t\t{maxima_5[0][i]}\t\t{abs(round(maxima_5[0][i]-maxima_6[0][i],4))}\n")
    f.write("\n\tvariance minima\t\tvariance maxima\n")
    f.write(f"FAR\t{variance_min_5}\t{variance_max_5}\n")
    f.write(f"CLOSE\t{variance_min_6}\t{variance_max_6}\n")
    f.write("\namplitudes in Kelvin (from fitted e-function to peak)\n")
    f.write("aluminum wide FAR (A1_aluminum)\n")
    f.write("t\tΔT (amplitude)\n")
    for i in range(len(amps_5)):
        f.write(f"{maxima_5[0][i]}\t{amps_5[i]}\t\n")
    f.write("\naluminum wide CLOSE (A2_aluminum)\n")
    f.write("t\tΔT (amplitude)\n")
    for i in range(len(amps_6)):
        f.write(f"{maxima_6[0][i]}\t{amps_6[i]}\t\n")
    f.write(f"\nthermal conductivity aluminum = {uthermal_conductivity_aluminum}\n")
    

# steel
with open(f'{make_string}data/phase_amps_tc_variances_steel.txt', 'w') as f:
    f.write("phase difference Δt\n")
    f.write("maxima_close\tmaxima_far\tΔt\n")
    for i in range(len(maxima_8[0])):
        f.write(f"{maxima_7[0][i]}\t\t{maxima_8[0][i]}\t\t{abs(round(maxima_8[0][i]-maxima_7[0][i],4))}\n")
    f.write("\n\tvariance minima\t\tvariance maxima\n")
    f.write(f"FAR\t{variance_min_8}\t{variance_max_8}\n")
    f.write(f"CLOSE\t{variance_min_7}\t{variance_max_7}\n")
    f.write("\namplitudes in Kelvin (from fitted e-function to peak)\n")
    f.write("steel wide FAR (A1_steel)\n")
    f.write("t\tΔT (amplitude)\n")
    for i in range(len(amps_8)):
        f.write(f"{maxima_8[0][i]}\t{amps_8[i]}\t\n")
    f.write("\nsteel wide CLOSE (A2_steel)\n")
    f.write("t\tΔT (amplitude)\n")
    for i in range(len(amps_7)):
        f.write(f"{maxima_7[0][i]}\t{amps_7[i]}\t\n")
    f.write(f"\nthermal conductivity steel = {uthermal_conductivity_steel}\n")
    

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