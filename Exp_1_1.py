import numpy as np
arr=np.array([[10,20,],
              [40,50],
              [70,80]])
newarr=arr.reshape((2,3))
print(newarr)
print(arr.shape())