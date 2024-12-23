import numpy as np

array=np.array([1,2,3])
print(array)

a=np.array([[1,2,3],[4,5,6]],ndmin=3)
print(a)

print(a.shape)
print(a.size)
print(a.ndim)
print(a.dtype)


b=np.zeros(shape=(2,3))
print(b)
c=np.ones(shape=(2,3))
print(c)


x = np.array([[1, 2], [3, 4]])

y = np.array([[5, 6]])

print(np.concatenate((x, y), axis=0))

