import numpy as np

x = np.genfromtxt("../data/viskositäten_kl.csv",delimiter=",",unpack=True,usecols=0)
average=0.001173219
y=0
for elem in range(x.size):
    y=y + (x[elem]-average)**2
y = y/(x.size-1)
sigma=y**(1/2)
print(sigma)