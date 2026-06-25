import numpy as np
# create array from list

#list 1d
# l = [1,2,3] 
# print(l)

#array 1d
# arr = np.array(l)
# print(arr)

# 2d list
# l = [[1,2,3], [4,5,6], [7,8,9]]
# print(l)

#2d array
# array = np.array(l)
# print(array)

# Question-> list 2d replace 4 by 100
# l = [[1,2,3], [4,5,6]]
# l[1][0] = 100
# print(l)

# print(np.array(l))

""" list vs numpy array
    1. Example of multi with list and array
    2. time comparision -> numpy array take less time than list
    3. zeros (3,4)
    4. ones (2,3)
    5. full ((2,2),7)
    6. random (2,3)
    7. arrange (0,10,2)

"""
#list
# l = [1,2,3]
# lm = l * 2
# print(lm)

# array
# arr = np.array(l)
# arrM = arr * 2
# print (arrM)

# Comparision
# import time
# list
# start = time.time()
# l = [i*2 for i in range(1000000)]
# print("list output:",time.time() - start)
 
# array
# start = time.time()
# arr = np.array(1000000)*2
# print("array output:",time.time() - start)

# zeros -> 
# zeros array in 1d
# arr = np.zeros(5)
# print(arr)

# zeros array 2d
# arr1 = np.zeros((3,4))
# print(arr1)

# ones array 1d
# arr = np.ones(5)
# print(arr)

# ones array 2d
# arr1 = np.ones((3,4))
# print(arr1)

# Question -> use zeros to make 2d array and plus every element with 10
# arr = np.zeros((3,4))
# print(arr + 10)

# Question -> use ones to make 2d array and multiply every element with 5
# arr1 = np.ones((3,4))
# print(arr1 * 5)

# full for 1d
# arr = np.full((3),5)
# print(arr)

# full for 2d
# arr1 = np.full((2,3),5)
# print(arr1)

# Question -> 

# arr = np.zeros((3,4))
# print(arr + 6)

# arr1 = np.full((3,4),1)
# print(arr1)

# random for 1d
# arr = np.random.random(5)
# print(arr)

# random for 2d
# arr1 = np.random.random((2,3))
# print(arr1)

# arrange for 1d
# arr = np.arange(5)
# print(arr)

# arrange for 1d || to convert into 2d -> reshape()
# arr1 = np.arange(0,10,2)  # start, stop, size
# print(arr1)

"""Vector, Matrix , Tensor
 array/list in 1d -> vector
 array/list in 2d -> matrix
 array/list in 3d -> tensor
"""
# l = [1,2,3] # vector list
# print(l)
# arr = np.arange(3) # vector array
# print(arr)

# l1 = [[1,2],[3,4]] # matrix list
# print(l1)
# arr1 = np.arange(4).reshape(2,2) # matrix vector
# print(arr1)

# l2 = [[[1,2],[3,4]],[[5,6],[7,8]]] # tensor list
# print(l2)

# arr2 = np.arange(8).reshape(2,2,2) # tensor vector
# print(arr2)

""" Array properties 
    1. Shape
    2. dimension
    3. size
    4. dtype
"""

# Array 1d
arr = np.arange(11)
print("Shape: ",np.shape(arr))
print ("dimension: ",np.ndim(arr))
print ("size: ", np.size(arr))
print("datatype: ",arr.dtype)

# Array 2d
arr1 = np.arange(12).reshape(3,4)
print("Shape: ",np.shape(arr1))
print ("dimension: ",np.ndim(arr1))
print ("size: ", np.size(arr1))
print("datatype: ",arr1.dtype)

