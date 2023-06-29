# 2.3.1
import numpy as np
array1 = np.array([1,2,3])
print('array 타입: ',type(array1))
print('array 형태: ',array1.shape)
array2=np.array([[1,2,3],[2,3,4]])
print('array 타입: ',type(array2))
print('array 형태: ',array2.shape)

# 2.3.2
array_int = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(type(array_int))
print(array_int.dtype)
print(array_int.ndim)
print(array_int.shape)
array_float = array_int.astype('float')
print(array_float)
print(array_float.dtype)

# 2.3.3
array1d = np.arange(start=1,stop=10)
array1d[0] = 9
array1d[8] = 0
print(type(array1d[0]))
print(array1d)
array2d = array1d.reshape(3,3)
print(array2d)
print('(0,0) 값 :',array2d[0,0])
print('(2,2) 값 :',array2d[2,2])

# 2.3.4
array1 = np.arange(start=1,stop=10)
array2 = array1[:3]
print(array2)
print(type(array2))
array2d = array1.reshape(3,3)
print(array2d)
print('row: 0~1, col: 0~1 까지의 값:\n',array2d[0:2,0:2])
print('row: 1~2, col: 0~3 까지의 값 : \n',array2d[1:3,:])
print('row : 0~1, col : 0 까지의 값 : \n', array2d[:2, 0])
