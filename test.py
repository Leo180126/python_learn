import numpy as np 
a = np.random.rand(3, 5, 5)
print(a)
a = a.reshape(-1)
print(a)
a = a.reshape(3, 5, 5)
print(a)
print(a.shape[2])