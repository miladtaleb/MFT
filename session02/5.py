import numpy as np
arr = np.random.rand(2,2)
brr = arr.copy()
print("Both arrays are 2*2 => ",arr.shape, brr.shape,"\nSo result is: ")
crr = np.matmul(arr,brr)
print(crr)