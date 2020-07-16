import numpy as np

def f12(x):
    m=(75-102)/0.52
    return m*(x-6.48)+102

x12=np.linspace(6.48,6.96,7)
print(x12,f12(x12))