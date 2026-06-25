"""Sorting
    sort() in 1d
    sort() in 2d -> use axis = 1 as columns and axis = 0 as rows
"""
import numpy as np 

# 1d

# arr = np.array([10,40,30,60,90,7,5])
# print(arr)
# arr_s = np.sort(arr)
# print(arr_s)

# 2d
# arr1 = np.array([[5,60,20],[40,90,4]])
# print(arr1)
# arr1_s = np.sort(arr1,axis= 0)
# arr1_s = np.sort(arr1,axis=1)
# print(arr1_s) # default sort -> rows

# example
# arr1 = np.array([[90,5,10],[20,2,15],[40,30,95]])
# print(arr1)
# arr1_s = np.sort(arr1)
# print(arr1_s)

# question
# arr_d = np.sort(arr1)[:,:: -1]
# print("Descending Order:", arr_d)
# arr_a = np.sort(arr1)
# print("Ascending Order: ", arr_a)

# filter

# 1d
# arr = np.array([10,20,40,6,4,2])
# print(arr)
# arr_f = arr[arr < 40]
# print(arr_f) 

# example
# arr = np.array([5,6,7,8,9])
# print(arr)
# arr_f = arr[arr % 2 == 0]
# print(arr_f)

""" Fancy indexing vs np.where()
    1. array(list)
    2. array([0,1,2])
    3. np.where(expression) -> ternary operation
    4. np.where(array>2)
    5. np.where(array > 2, array*2, array)
    6. np.where(array > 2 , "True", "False")
"""

# Fancy indexing
# arr = np.array([10,20,3,4,90,100])
# print(arr)
# arr_f = arr[[0,2]]
# print(arr_f)

# arr1_f = arr[arr % 2 == 0]
# print(arr1_f)

# np.where()
# 1d
# arr = np.array([10,3,4,80,30,40,9])
# print(arr)
# arr_w = np.where(arr >40)
# print(arr_w)
# arr1_w = np.where(arr>40,"True","False")
# print(arr1_w)

# example
# arr_w = np.where(arr > 40 , arr+2,arr-2)
# print(arr_w)

# concatenate
# 1d
# arr1 = np.array([10,20,30])
# arr2 = np.array([1,2,3])
# arr1_arr2 = np.concatenate((arr1,arr2))
# print(arr1_arr2)
# arr1_arr2_new = arr1 + arr2
# print(arr1_arr2_new)

# 2d
# arr2= np.array([[3,4,7,2],[5,8,9,14]])
# arr3= np.array ([[32,3,6,4],[7,86,47,3]])
# arr_new1= np.concatenate((arr2,arr3))
# print(arr_new1)

""" Statistical Functions
    1.  np.sum(a) -> Sum of all elements
    2.  np.mean(a) -> Average = Sum of elements / Number of elements
    3.  np.median(a) -> Middle value after sorting
    4.  np.min(a) -> Smallest value in array
    5.  np.max(a) -> Largest value in array
    6.  np.var(a) mean,difference,square,average | (sum = ddof) -> divide by array length
    7.  np.std(a) -> Standard Deviation = √Variance -> Measures spread of data
    8.  np.prod(a) -> Multiplication of all elements
    9.  np.cumsum(a) -> Cumulative (running) sum
    10. np.cumprod(a) -> Cumulative (running) product
    11. np.argmin(a) -> Index position of minimum value
    12. np.argmax(a) -> Index position of maximum value
    13. np.abs(a) -> Converts negative values to positive -> Absolute value (distance from zero)
    14. np.unique(a) -> Returns unique values only -> Removes duplicates
    15. np.percentile(a, 50) -> Finds percentage-based value -> 50th percentile = Median
    16. np.quantile(a, 0.5) -> Similar to percentile -> 0.5 = 50%
    17. np.ptp(a) -> Range = Max - Min
    18. np.any(a) -> True if at least one value is True
"""
# arr = np.array([10,30,20,40,70])
# add = np.sum(arr)
# print(add)
# average = np.mean(arr)
# print(average)
# median = np.median(arr)
# print(median)
# smallest = np.min(arr)
# print(smallest)
# largest = np.max(arr)
# print(largest)
