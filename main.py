import numpy as np
z = np.arange(36).reshape(3,4,3)
print(z.shape)
print(z)
print(z.sum(axis = 0))