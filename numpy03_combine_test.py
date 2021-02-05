import numpy as np

b = np.arange(12)
# 与reshape一样，但直接修改所操作的数组
b.resize((4, 3))
print(f'b = \n{b}')

c = b * 2
print(f'\nc = \n{c}')

# 水平组合数组
d = np.hstack((b, c))
print(f'\n水平组合b和c:\n{d}')

# 垂直组合数组
e = np.vstack((b, c))
print(f'\n垂直组合b和c-01:\n{e}')

# 同vstack
f = np.concatenate((b, c), axis=0)
print(f'\n垂直组合b和c-02:\n{f}')

# 深度组合，沿着纵轴（深度）方向层叠组合
g = np.dstack((b, c))
print(f'\n深度组合b和c:\n{g}')

one = np.arange(2)
twice_one = one * 2

# 将一维数组按列方向进行组合，对于二维数组，与hstack相同
h = np.column_stack((one, twice_one))
print(f'\n列组合one和twice_one:\n{h}')
# 将一维数组按行方向进行组合，对于二维数组，与vstack相同
i = np.row_stack((one, twice_one))
print(f'\n行组合one和twice_one:\n{i}')
