# OOPs Concepts in python
"""
OOPs concept are :-
     1.Class 
     2.Object 
     3.Inheritance 
     4.Polymorphism
     5.Encapsulation
     6. Abstraction
"""

# Example
# class Harsh:
#     def __init__(self, name):  # _init_ is a constructor
#         self.name = name 
#     def show (self) :    # self refers to the current object of the class
#         print(self.name)
# r= Harsh("Hello") # creating an object of class Harsh
# r.show()

# Example 2 :
# class Harsh:
#     def __init__(self):
#         print(" calling constructor")
#     def show(self):
#         print("Hello")
# r = Harsh()
# r.show()

# Example 3 :
# class Harsh:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def getAge(self):
#         print("My age is: ",self.age)
#     def getName(self):
#         print("My name is: ", self.name)
# r = Harsh("Harsh", 20)
# r.getAge()
# r.getName()

# Example 4 :
# class student:
#     def __init__(self, *args):
#         print(type(args))
#         self.name = args[0]
#     def getStu(self):
#         print("the student is: ", self.name)
#         return self.name
# s = student("Hello", 20 , "00000000", " arya@main")
# s.getStu()

# t = s.getStu()
# print(t)

# Example 5 :
# class college:
#     def __init__(self, name):
#         self.name = name['name']
#         self.location = name["location"]
#     def getCollege(self):
#         print("The college name is: ", self.name)
#         print("The college location is: ", self.location)
# c = college({"name": "GRASS", "location": "Bangalore"})
# c.getCollege()

# Example 6 :
# class student:
#     def __init__(self, *args):
#         self.data = args 
#     def users(self):
#         return self.data[0]
#     def details(self):
#         return self.data[1]
# s = student (["dheeraj","kunal","harsh"],{"address":"kukas","college": "arya", "location": "jaipur"})
# u = s.users()
# for i in s.users():
#     print(i)
# d =s.details()
# for i in s.details():
#     print(i, ":", s.details()[i])

# Example 7 :
# class Student:
#     def __init__(self, **data):  # **data or **kwargs is used for collects keyword argument into a dictionary 
#         self.data = data
# s = Student(name="Harsh", age=20)
# print(s.data)
