import numpy as np

a = np.arange(9).reshape((3, 3))

print(f'a = \n{a}')

b = np.hsplit(a, 3)
print(f'\n水平分割:\n{b}')

c = np.split(a, 3, axis=1)
print(f'\n水平分割2:\n{c}')

d = np.vsplit(a, 3)
print(f'\n垂直分割:\n{d}')

e = np.split(a, 3, axis=0)
print(f'\n垂直分割2:\n{e}')

f = np.arange(27).reshape((3, 3, 3))
print(f'\nb = \n{f}')

g = np.dsplit(f, 3)
print(f'\n深度分割:\n{g}')
