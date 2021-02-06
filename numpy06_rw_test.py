import numpy as np

i2 = np.eye(2)

print(i2)
#np.savetxt('eye.txt', i2)

c, v = np.loadtxt('data.csv', delimiter=',', usecols=(6, 7), unpack=True)

vwap = np.average(c, weights=v)
print(f'VWAP = {vwap}')

mean = np.mean(c)
print(f'mean = {mean}')

t = np.arange(len(c))
twap = np.average(c, weights=t)
print(f'TWAP = {twap}')

h, l = np.loadtxt('data.csv', delimiter=',', usecols=(4 ,5), unpack=True)
print(f'highest: {np.max(h)}')
print(f'lowest: {np.min(l)}')

print(f'Spread high price: {np.ptp(h)}')
print(f'Spread low price: {np.ptp(l)}')