import numpy as np

a = np.arange(24).reshape((6, 4))

print(f'数组a的维数:{a.ndim}')

a = a.reshape((2, 3, 4))
print(f'数组a的维数: {a.ndim}')

print(f'\n数组a的元素总个数: {a.size}')

print(f'\n数组a中元素在内存中所占的字节数: {a.itemsize}')

print(f'\n数组a的大小: {a.nbytes}')

a = a.reshape((6, 4))

# T属性的效果与transpose一样
print(a.T)

a = a.flatten()

# 一维数组的T属性就是原数组
print(a.T)

b = np.array([1.j + 1, 2.j + 3])
print(b)

print(f'\n数组b的实部: {b.real}')

print(f'\n数组b的虚部: {b.imag}')

a = a.reshape((6, 4))

print('\n遍历数组a:\n')
for item in a.flat:
    print(item, end=' ')
print('')

print('\n从flatiter对象直接获取一个数组元素: ', end='')
print(a.flat[2])

print('\n获取多个: ', end='')
print(a.flat[[1, 3]])

print('\n对flat属性赋值:')
a.flat = 8
print(a)

print('\n选择多个元素赋值: ')
a.flat[[1, 3]] = 1
print(a)