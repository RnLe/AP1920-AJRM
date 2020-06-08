import numpy as np

x = np.genfromtxt("../data/viskositäten_kl.csv",delimiter=",",unpack=True,usecols=0)
ave=0
for elem in range(x.size):
    ave = ave + x[elem]

print(ave/x.size)