import numpy as np

i2 = np.eye(2)

print(i2)
#np.savetxt('eye.txt', i2)

c, v = np.loadtxt('data.csv', delimiter=',', usecols=(6, 7), unpack=True)
print(c, v)
vwap = np.average(c, weights=v)
print(f'VWAP = {vwap}')

mean = np.mean(c)
print(f'mean = {mean}')

t = np.arange(len(c))
twap = np.average(c, weights=t)
print(f'TWAP = {twap}')