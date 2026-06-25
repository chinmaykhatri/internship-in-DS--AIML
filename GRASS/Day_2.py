# #type conversion
# num =(input("Enter a number: "))
# print(num)
# print(type(num))
# print(int(num) + 10) # all are integer values
# print(num + str(10)) # all are string values
# print(num + 10)  # num num num num -> value of num variable

# Operators & Expressions
#arithmatic operators
# + - * / // \\ **
# print(10 +20) #Addition
# print(20 - 10) # substraction
# print(10 * 2)  #multiplication
# print(20 / 2) # division
# print(20 // 3) # floor division
# print(2 ** 3) # exponentiation
# print(10 % 3) # modulus

# num = (int(input("Enter a number : ")))
# print ( "Even" if num % 2 == 0 else "Odd" )

#Realtional operators
# == != > < >= <=
# num1 = 10
# num2 = 11
# print(num1 == num2) # equal to
# print(num1 != num2) # not equal to
# print(num1 > num2) # greater than
# print(num1 < num2) # less than
# print(num1 >= num2) # greater than or equal to
# print(num1 <= num2) # less than or equal to

# Assignment operators
# = += -= *= /= //= **= %=
# num1 = 10
# num2 = num1 # assignment operator
# print(num2)
# num2 += 5  # num2 = num2 + 5
# print(num2)
# num2 -= 5 # num2 = num2 - 5
# print(num2)
# num2 *= 5 # num2 = num2 * 5
# print(num2)
# num2 /= 5  # num2 = num2 / 5
# print(num2)
# num2 //= 5 # num2 = num2 // 5
# print(num2)
# num2 **= 5 # num2 = num2 ** 5
# print(num2)
# num2 %= 5 # num2 = num2 % 5
# print(num2)

# logical operators
# and, or, not
# a = 10
# b = 20
# print(a and b) # and operator
# print(a or b) # or operator
# print(not a) # not operator

# name1 = "Hello"
# name2 = ""
# print(name1 and name2)
# print(name1 or name2)
# num1 = [] #default [] -> false || [1,2,3] -> true
# print(not num1)

# ------- Day 3 -------

# bitwise operators
# & | ^ ~ << >>
# a= 5
# b= 2
# print (a & b) # bitwise and
# print (a | b) # bitwise or
# print (a ^ b) # bitwise xor
# print (~a) # bitwise not
# print (a << 1) # bitwise left shift
# print (a >> 1) # bitwise right shift

# identity operators
# is, is not
# name = "Hello"
# print(name is "Hello") # identity operator
# print(name is not "Hello") # identity operator

# num1 = -5
# num2 = -4
# print(num1 is num2)

# -5 to 256 -> both  variable will point to same memory location
# num1 = 270
# num2 = 270
# print(num1 is num2)
# print (id(num1))
# print (id(num2))