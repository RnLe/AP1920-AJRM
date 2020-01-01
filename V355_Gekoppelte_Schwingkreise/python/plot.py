import matplotlib
import matplotlib.pyplot as plt
import numpy as np

N = 8

f_minus = [33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1]
f_plus = [81.3,61.1,57.1,48.7,44.7,42.8,41.4,40.2]
c_k = [1.0 ,2.2 ,2.7 ,4.7 ,6.8 ,8.2 ,10.0,12.0]
vol_cur = [0.038,0.041,0.039,0.043,0.045,0.038,0.042,0.042]
expec = [0.038,0.041,0.039,0.043,0.045,0.038,0.042,0.042]

fig, ax = plt.subplots()
ax2 = ax.twinx()

ind = np.arange(N)
width = 0.15
p1 = ax.bar(ind, f_minus, width, bottom=0)
p2 = ax.bar(ind+width, f_plus, width, bottom=0)
p3 = ax.bar(ind+2*width, c_k, width, bottom=0)
p4 = ax2.bar(ind+3*width, vol_cur, width, bottom=0, color='r')

ax.set_xticks(ind + width/5)
ax.set_xticklabels(c_k)

#ax.legend((p1[0], p2[0], p3[0], p4[0], p5[0], ('f-', 'f+', 'Ck', 'I2', 'Itheo')))
ax.autoscale_view()

plt.show()