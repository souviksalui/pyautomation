import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)

print('shape of array :', arr.shape)

print('dimension of array :', arr.ndim)

print('size of array :', arr.size)

print('dtype of array :', arr.dtype)

print('itemsize of array :', arr.itemsize)

print('nbytes of array :', arr.nbytes)

arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr2.shape,arr2.ndim,arr2.size,arr2.dtype,arr2.itemsize,arr2.nbytes)