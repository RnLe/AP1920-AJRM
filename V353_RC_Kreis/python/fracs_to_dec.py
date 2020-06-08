import numpy as np

zaehler = np.genfromtxt("../data/zaeh.csv",delimiter=",",unpack=True,usecols=0)
nenner = np.genfromtxt("../data/nenn.csv",delimiter=",",unpack=True,usecols=0)

for elem in range(zaehler.size):
    print(zaehler[elem]/nenner[elem])