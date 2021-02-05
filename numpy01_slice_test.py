import numpy as np

a = np.arange(24)

print(a)
b = a.reshape(2, 3, 4)
print(b)
print(b.shape)

print('选取所有楼层的第1行、第1列的房间')
print(b[:, 0, 0])
print('')

print('选取第1层楼的所有房间')
print(b[0])
print('')

print('同上')
print(b[0, :, :])
print('')

print('同上')
print(b[0, ...])
print('')

print('选取第1层、第2排的房间')
print(b[0, 1])
print('')

print('在上面的数组切片中间隔地选定元素')
print(b[0, 1, ::2])
print('')

print('选取所有楼层地位于第2列地房间')
print(b[..., 1])
print('')

print('选取所有位于第2行地房间')
print(b[:, 1])
print('')

print('选取第1层楼的所有位于第2列的房间')
print(b[0, :, 1])
print('')

print('选取第1层楼的最后一列的所有房间')
print(b[0, :, -1])
print('')

print('在上面数组切片中间隔地选定元素')
print(b[0, ::2, -1])
print('')

print('反向选取第1层楼的最后一列的所有房间')
print(b[0, ::-1, -1])
print('')

print('把第1层的房间和第2层的房间交换')
print(b[::-1])
