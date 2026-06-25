""" Array Reshaping 
    1. reshape()
    2. faltten() -> create copy
    3. ravel() -> return original
    4. transpose
"""
 # reshape array
import numpy as np
# arr = np.arange(12)
# up_arr = np.reshape(arr,(3,4))
# print(up_arr)

# example
# arr = np.arange(15).reshape(5,3)
# print(arr)

# example
# arr = np.arange(27)
# up_arr = np.reshape(arr,(3,3,3))
# print(up_arr) 


# flatten -> it is used for convert 2d and 3d array into 1d array and 
# if any change happen after flatten apply then it only changes in copy array 

# arr = np.arange(12).reshape(3,4)
# print(arr)
# up_arr = arr.flatten()
# up_arr = 100
# print(up_arr)

# example of 3d flatten
# arr = np.arange(27).reshape(3,3,3)
# print(arr)
# up_arr = arr.flatten()
# print(up_arr)

# ravel -> it is used to convert 2d & 3d array into 1d array and if any changes want to 
# happen then it changes in copy array as well as original array

# arr = np.arange(12).reshape(3,4)
# print(arr)
# up_arr = arr.ravel()
# up_arr = 100
# print(up_arr)

# example 3d
# arr = np.arange(24).reshape(2,3,4)
# print(arr)
# up_arr = arr.ravel()
# print(up_arr)

# transpose
# arr = np.arange(12).reshape(3,4)
# print(arr)
# up_arr = arr.T
# print(up_arr)

# example 3d
# arr = np.arange(24).reshape(2,3,4)
# print(arr)
# up_arr = arr.T
# print(up_arr)


# slicing for 1d 
# arr = np.arange(12)
# print(arr)
# up_arr = arr[:3]
# print(up_arr)

# slicing for 2d
# arr = np.arange(12).reshape(3,4)
# print(arr)
# up_arr = arr[:,3]
# print(up_arr)

# slicing for 2d
# arr = np.arange(24).reshape(2,3,4)
# print(arr)
# up_arr = arr[:,:1,:2]
# print(up_arr)

# Question -> slicing for 3d -> arange(24) -> 0,23
# arr = np.arange(24).reshape(2,3,4)
# print(arr)
# up_arr = arr[0,0,0]
# print(up_arr)
# up_arr = arr[1,2,3]
# print(up_arr)
# print(arr[:1,:1,:1],arr[1:2,2:3,3:4])

""" Looping in Numpy
      while loop
      for loop
"""
# while loop :
# for 1d
# arr = np.arange(12)
# i = 0
# while i< len(arr):
#     print(arr[i], end = " ")
#     i += 1

# for 2d
# arr1 = np.arange(12).reshape(3,4)
# i = 0
# while i < arr1.shape[0]: 
#     j = 0
#     while j < arr1.shape[1]: 
#         print(arr1[i, j], end=" ")
#         j += 1
#     print()
#     print("\n")
#     i += 1

#for 3d
# arr2 = np.arange(24).reshape(2,3,4)
# i = 0
# while i< arr2.shape[0]:
#     j = 0 
#     while j <arr2.shape[1]:
#          k = 0
#          while k < arr2.shape[2]:
#               print(arr2[i,j,k], end = " ")
#               k += 1
#          print("\n")
#          j += 1
#     print()
#     print("\n")
#     i += 1


# for loop for 1d array
# arr = np.arange(12)
# i = 0
# for i in range(len(arr)):
#     print(arr[i], end = " ")
#     i += 1

#for loop for 2d array 
arr1 = np.arange(12).reshape(3,4)
i = 0
for i in range(arr1.shape[0]):
    j = 0
    for j in range(arr1.shape[1]):
        print(arr1[i,j], end = " ")
        j += 1
    print()
    i += 1  