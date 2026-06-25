#------Numpy------
"""
Comparision between numpy and list

        list                                Numpy
    1. datatype -> multi then                 1. Datatype -> single
       it is used.                                then it is used.
    ex. [True,"hello",100]                    ex. [10,20,30]
    2. list                                   2. Array
    ex. l[0] -> True                          ex. a[0] -> 10
    3. list have not many method              3. Numpy have so many in-built
       not present in python.                    methods are present in python.
In Javascript, we want to import any package then we want to write 
"npm i packagename".
In python, we want to install or import any libraries then we write
"pip install packagename"
"""

import numpy

# n = numpy.arange(11)
# print(type(n))
# print(n)

# print(n[0])

#example 
# n = numpy.arange(12)
# d = n.reshape(3,4) # 3 -> rows or 4-> columns
# print(type(d))
# print(d)

# example 2d
# n = numpy.arange(12).reshape(4,3)
# print(n)

# example 3d
# t = numpy.arange(27).reshape(3,3,3)
# print(t)

# t = numpy.arange(24).reshape(2,3,4)  # 2 -> outer rows 3 -> inner rows 4 -> inner columns
# print(t)

# n = numpy.arange(12).reshape(4,3)
# print(n[:,2])  # : -> means select all rows and 2 -> select column index 2
# print(n[0:1,:]) # means select row 0 only and all column also be selected
# print(n[1:3,1]) # output will [4,7]
