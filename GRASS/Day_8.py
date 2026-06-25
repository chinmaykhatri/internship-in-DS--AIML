#Class methods and self

# class address:
#     def __init__(self, city, state):
#         self.city = city
#         self.state = state
#     def show(self):
#         print("The city is: ", self.city)
# a = address("jaipur", "rajasthan")
# a.show()

# Inheritance

# class address:
#     def __init__(self, city, state):
#         self.city = city
#         self.state = state
#     def location(self):
#         return f" the city is {self.city} in {self.state}"
# class user(address):
#     def __init__(self,name,age,city,state):
#         self.name = name 
#         self.age = age
#         # self.city = city   # we can also use super() to call the parent class constructor instead of writing the variable
#                              # again in child class constructor
#         # self.state = state
#         super().__init__(city, state)
#     def userName(self):
#         print (f"my name is {self.name}")
# u= user("harsh",20,"jaipur","rajasthan")
# u.userName()
# print(u.location())

# Encapsulation

# class address:
#     def __init__(self,city,state):
#         self.__city = city # private attribute
#         self.state = state
#     def location(self):
#         print(f"the city is {self.__city} in {self.state}")
#     def get_city(self):
#         return self.__city
# a = address("chhapra", "bihar")
# a.location()
# print (a.__city) #error show because __city is private attribute and we cannot access it outside the class but we can access it through a public method like get_city() which is defined in the class address.
# print(a.get_city())
# print(a.state)

#Polymorphism

# class address:
#     def __init__(self, city, state):
#         self.city = city
#         self.state = state
#     def location(self):
#         print (f" the city is {self.city} in {self.state}")
# class homeTown(address):
#     def __init__(self,city,state):
#         self.city = city
#         self.state = state
#     def location(self):
#         print (f" the home town is {self.city} in {self.state}")
# a = address("vadora", "gujarat")
# a.location()
# b = homeTown("chhapra", "bihar")
# b.location()

#class variables
# class address:
#     total = 0 # class variable
#     def __init__(self, city, state):
#         self.city = city
#         self.state = state
#         address.total += 1
#     def location(self):
#         print("location")
# a= address("jaipur", "rajasthan")

# b= address("chhapra", "bihar")
# a.location()
# print(address.total)

# overloading and overriding

""" Generally overloading is not supported in python. Because first function overwrite by second function.
    Method overriding is a feature of object-oriented programming that allows a subclass to provide a specific implementation of a method 
    that is already defined in its superclass.The method in the subclass has the same name, return type, and parameters as the method in 
    the superclass. When the method is called on an instance of the subclass, the overridden method in the subclass is executed
"""
# def address(city, state):
#     print(f"my address is {city} in {state}")

# def address(city, state, country):
#     print(f"my address is {city} at {state} in {country}")
# # address("jaipur", "rajasthan") # Error show because the second function is overriding the first function and we cannot have two functions with same name in python.
# address("jaipur", "rajasthan", "india")
 
# class address:
#     def __init__(self, city, state):
#         self.city = city
#         self.state = state
#     def location(self):
#         print("location")
# class user(address):
#     def __init__(self,name,age,city,state):
#         self.name = name 
#         self.age = age
#     def location(self):  #method overriding
#         print ("user location")
# u = user("arya mains",20,"jaipur","rajasthan")
# u.location()

# Tuples
""" Tuples are immutable(not changable) data structure in python."""
# t = (10,20,30)
# print(t[0])
# print(t[-1])

# example
# marks = [98,90,80,95]

#list -> change
# marks[3] = 50
# print(type(marks))
# print(marks)

#tuple -> not change
# t = tuple(marks)
# print(type(t))
# print(t)

#tuple into list
# m = list(t)
# print(type(m))
# print(m)