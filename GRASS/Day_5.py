# Dictionary methods
""" 1.get()
    2.keys()
    3.values()
    4.items()
    5.update()
    6.clear()
    7.copy()
    8.del
"""
# d = {'name': 'hello', 'age': 20}
# d.update({'name': 'arya'})
# d['name'] = 'arya mains'
# del d['name']
# print(d)

# Nested dictionary
# d = {"address": {"address1": {"city": "kukas city", " district": "jaipur"},
#                  "address2": {"city": "gopalpura", "district": "arya mains"}}}
# print(d['address']['address1']['city'])    #first method
# print(d['address']['address1'][' district'])
# print(d['address']['address2']['city'])
# print(d['address']['address2']['district'])

# for i in d.values(): #second method
#     for j in i.values():
#         for  k in j.values():
#             print(k)


# Nested list

# l = [10,20,30,["hello","hello1","hello2",[True,False]]]
# for i in range(len(l)):
#     if type(l[i]) == list:
#         for j in range(len(l[i])):
#             if type(l[i][j]) == list:
#                 for k in range(len(l[i][j])):
#                     print(l[i][j][k])
#             else:
#                 print(l[i][j])
#     else:
#         print(l[i])


# Slicing in list

# l1 = l[:3]
# print(l1)

#Because slicing moves left to right by default. 
# Here start index comes after end index, so nothing is selected.
# l1 = l[-1:-3]
# print(l1)


# def square(x):
#     return x*x

# Map(Transform values)
# l = [10,20,30]
# l1 = list(map(square,l))
# print(l1)

#Filter(Select values)
# def helo(x):
#     return x.endswith('a')
# l = ["apple","banana","cat","dog"]
# l2 = list(filter(helo,l))
# print(l2)

#example | alternative of filter 

# l1 = []
# for i in l:
#     if 'a' == i[-1]:
#         l1.append(i)
# print(l1)

# example
# l=["apple","banana","cat","dog"]
# upper_words = list(map(str.upper, l))
 
# print(upper_words)


#reduce(Combine values)

#File handling & Exception handling
#--------exception handling---------------
#try except
# try:
#     num1 = 10
#     num2 = 5
#     print (num1/num2)
# except :
#     print("hello except")

# try :
#     num1 = 10
#     num2 = 0
#     print (num1/num2)
# except:
#     print("hello except")

# try except and finally
# try:
#     num1 = 10
#     num2 = 0
#     print (num1/num2)
# except:
#     print("hello except")
# finally:
#     print("hello finally")