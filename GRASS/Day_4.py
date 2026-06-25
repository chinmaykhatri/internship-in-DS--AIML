# ❤ Function
# def hello():
#     print("hello function is working")
# hello()


# def hello(a): # a is a parameter
#     print(a)
# hello(100) # 100 is a argument

#-----------Example------------

# def add(a,b):
#     print(a+b)
# add(5,10)
# add()

#-----------Example------------

# def power(a,b):
#     print(a**b)

# power(5,2)
# power(2,5)
# power(b=5,a=2)


#----------Example-----------
# def student(*a):
#     print(a)
#     print(type(a))
#     print(a[0])

# def student(a,b):
#     print(a,b)

# student(10,20)
# student(1,2,3,4,5,6)

# In this situation where two function of same name is defined 
# then when we call function last function is valid

#---------Question--------
# def marks(a):
#     for i in range(len(a)):
#         print(a[i])
# marks([10,20,30,40,50])

#---------Question----------
# def address(a):
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             print(a[i][j])
# address(["hello","Harsh"])

#-----------Example------------

# def sum(a,b):
#     return a+b 
# result = sum(10,20)
# print(result)


# ❤ Lamda function [lamda argument:expression]
# add = lambda x: x
# print(add(100))

# sum = lambda a,b: a+b
# print(sum(10,20))

# a= lambda x: [i for i in x]
# print (a([1,2,3,4,5]))

# a = lambda *x: [i for i in x]
# print (a(10,20,30))

#List comprehensions[expression for item in iterable]
# print([i for i in  range(5)])

#----------example---------
# l = [10,20,30,40,50,60]
# print([l[i] for i in range(len(l))])

#--------Question--------
# l = [10,20,[30,40,50,60]]
# print ([l[2][i] for i in range(len(l[2]))])


#list
"""
l = [10,20,30]
l[0] -> 10
len(l) -> 3
l.append(40) -> [10,20,30,40]
l.insert(1,100) -> [10,100,20,30,40]
"""
# l = [10,20,30]
# print(l[0])
# print(len(l))
# l.append(40)
# print(l)
# l.insert(1,100)
# print(l)

#example for append
# l = ["hello","harsh","python"]
# l.append("for arya mains")
# print(l[0])
# print(l[-1])

#example for insert
# l = ["true","false",10,20]
# l.insert(1,100)
# print(l)

#------Question--------
# l= [10,20,30,{"name":"harsh","address":["jaipur","kukas","Tonk","bhilwara"]}]
# print(l[3]["address"][2])
# print(l)
# print(l[3])
# print(l[3]["address"])
# for i in l[3]["address"]:
#     print(i)

#---------Question---------
# l= [10,20,30,[40,50,[60,70,80]]]
# for i in range(0,2):
#     print(l[3][i])
# print(l[3][0])
# print(l[3][1])

"""
dictionary =>
d = {'name' : 'helllo'}
d['name'] -> hello
d.keys() -> ['name']
d.values() -> ['hello']
"""


# d= {'name' : 'hello', 'age' : 20}
# print(d.keys())
# print(d.values())
# for i in d.keys():
#     print("keys = ",i)
#     print("values = ",d[i])

#---------Question---------
# d = {
#   "Message": "Number of Post office(s) found: 6",
#   "Status": "Success",
#   "PostOffice": [
#     {
#       "Name": "Achrol",
#       "Description": "",
#       "BranchType": "Sub Post Office",
#       "DeliveryStatus": "Delivery",
#       "Taluk": "Jaipur",
#       "Circle": "Jaipur",
#       "District": "Jaipur",
#       "Division": "Jaipur Moffusil",
#       "Region": "Jaipur HQ",
#       "State": "Rajasthan",
#       "Country": "India"
#     },
#     {
#       "Name": "Jaitpura Khinchi",
#       "Description": "",
#       "BranchType": "Branch Post Office",
#       "DeliveryStatus": "Delivery",
#       "Taluk": "Jaipur",
#       "Circle": "Jaipur",
#       "District": "Jaipur",
#       "Division": "Jaipur Moffusil",
#       "Region": "Jaipur HQ",
#       "State": "Rajasthan",
#       "Country": "India"
#     },
#     {
#       "Name": "Kali Pahadi",
#       "Description": "",
#       "BranchType": "Branch Post Office",
#       "DeliveryStatus": "Delivery",
#       "Taluk": "Jaipur",
#       "Circle": "Jaipur",
#       "District": "Jaipur",
#       "Division": "Jaipur Moffusil",
#       "Region": "Jaipur HQ",
#       "State": "Rajasthan",
#       "Country": "India"
#     },
#     {
#       "Name": "Kant",
#       "Description": "",
#       "BranchType": "Branch Post Office",
#       "DeliveryStatus": "Delivery",
#       "Taluk": "Jaipur",
#       "Circle": "Jaipur",
#       "District": "Jaipur",
#       "Division": "Jaipur Moffusil",
#       "Region": "Jaipur HQ",
#       "State": "Rajasthan",
#       "Country": "India"
#     },
#     {
#       "Name": "Labana",
#       "Description": "",
#       "BranchType": "Branch Post Office",
#       "DeliveryStatus": "Delivery",
#       "Taluk": "Jaipur",
#       "Circle": "Jaipur",
#       "District": "Jaipur",
#       "Division": "Jaipur Moffusil",
#       "Region": "Jaipur HQ",
#       "State": "Rajasthan",
#       "Country": "India"
#     },
#     {
#       "Name": "Rajpurawas Tala",
#       "Description": "",
#       "BranchType": "Branch Post Office",
#       "DeliveryStatus": "Delivery",
#       "Taluk": "Jaipur",
#       "Circle": "Jaipur",
#       "District": "Jaipur",
#       "Division": "Jaipur Moffusil",
#       "Region": "Jaipur HQ",
#       "State": "Rajasthan",
#       "Country": "India"
#     }
#   ]
# }
# for i in d.values():
 
#     if type(i) == list:
 
#         for item in i:
 
#             for data in item.values():
#                 print(d.keys()," = ",data)
 
#     else:
#         print(d.keys()," = ",i)