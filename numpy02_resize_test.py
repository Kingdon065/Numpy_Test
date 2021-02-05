import numpy as np

a = np.arange(12).reshape(2, 2, 3)

print(f'a = \n{a}')

# 展平数组，返回数组的一个视图(view)
b = a.ravel()
print(f'\n展平数组a-01:\n{b}')

# 展平数组，请求分配内存来保存结果
c = a.flatten()
print(f'\n展平数组a-02:\n{c}')

# 使用一个正整数元组来设置数组的维度
a.shape = (3, 4)
print(f'\n重设数组a的维度-01:\n{a}')
# 转置数组
d = a.transpose()
print(f'\n转置数组a:\n{d}')

e = np.arange(12)
# 与reshape一样，但直接修改所操作的数组
e.resize((4, 3))
print(f'\n重设数组a的维度-02:\n{e}')