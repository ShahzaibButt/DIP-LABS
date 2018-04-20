import numpy as np

x = np.array((2,3,4))
print(x)
a = np.shape((2,3,4))
print(a)
b = np.zeros((2,3,4))
print(b.shape)
print(b)

c = np.ones((2,3,4))
print(c)

d = np.ones((2,3,4))
print(d*5)

y = np.arange(0,999)
print(y)


a = [2,3.2,5.5,-6.4,-2.2,2.4]
x = np.array(a)
print(x)
print(x[1])
print(x[1:4])

z = [[2, 3.2, 5.5, -6.4, -2.2, 2.4], [1, 22, 4, 0.1, 5.3, -9], [3, 1, 2.1, 21, 1.1, -2]]
x = np.array(z)
print(x)
print("-------------------------")
print(x[:, 3])
print(x[1:4, 0:4])
print(x[1:, 2])