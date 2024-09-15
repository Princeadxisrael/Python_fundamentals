import random

# indentation

# if 10 > 8:
#     print("Ten is greater's than five")
#     print("Ten is greater than five")

# # variable
# x=5
# y= "Hello, World"
# print(x)
# print(y)

# # casting
# v=str(3)
# w= int(3)
# u= float(3)
# print(v)
# print(w)
# print(u)

# print (type(v))

# X="Imelda"
# print(x, X)

#variable names
# A variable must start with a letter or an underscore
# A variable name can contain Alpha-numeric characters (A-z, 0-9, _)
# A variable name is case sensitive
# A variable name cannot be a keyword
# variable names are written in snakeCase

# myname="Abel"
# my_name="Abel"
# _my_name ="Abel"
# myName="Abel"
# MYNAME="Abel"
# myname2="Abel"

# #Assign many values to multiple variables
# x=y=z="Peter"
# print(x, y, z)


# fruits =["mango", "orange", "grapes"]
# X, Y, Z= fruits
# print(X,Y,Z)

# def myFunc():
#     global v
#     v="global"
#     print("Python is a " + v + " language")

# myFunc()

# print(v)

# Data types

#Text Type: str
# Numeric Type: int, float, complex
# Sequence Type: list, tuple, range
# Mapping Type: dict
# Set Type: set, frozenset
# Boolean Type: bool,
# Binary Types: bytearray, bytes, memoryview
# None Type: NoneType

# myVar= bool(5)

# print(type(myVar))
# # Numeric Type: int, float, complex
# #Integer is a whole number ranging fron -ve infinty to +ve infinity
# #Floating numbe is a postive or negative that contains one or more decimals e.g 3.2, 1.0, -30.0
# #complex number is a number with an imaginary time
# x= 3+ 5j
# print(type (x))


# print(random.randrange(1, 15))

# #Boolean 
# print(10 > 10)
# print(10 > 9)
# print(10 == 10)
# if type(x)=="complex":
#     print("x is a complex number")
# else:
#     print("x is just a regular number")

# print(bool("Hello"))
# print(bool(70))
# print(bool([]))

# #Falsy Value
# # Nan, undefined, None, zero, false, " ",

# def func():
#     return True

# if func():
#     print("YES")
# else:
#     print("NO")

# a=300
# print(isinstance(a, int))

#Operator
# +, -, *, /, %, **, //

# =, +=, -=, *=, /=, %=

# ==, !=, >, <, >=, <=

# and, or, not

# if a<5 or a> 305:
#     print("True")
# else:
#     print("Not true")

# #PEMDAS
# print((6+1)-6*1)

#Strings
# text= """lorem ipsum dolor sit amet
#         lorem ipsum dolor sit amet
#         lorem ipsum dolor sit amet"""
# print (text)

# a= "Hello, world"
# print(len(a))

# if "hello" not in a:
#     print("hello is not present")

# print(a[1:-1])
# print(a)

# print(a.strip())
# print(a.replace("world", "universe"))

# print (a.split(", "))

# a="Hello"
# b="World"
# c= a +" "+ b
# print(c)

# age= 15 * 2
# txt= f"My name is Kelvin, I am {age:.2f}"
# print(txt)

# text= "the biggest shipwreck was the \"titanic\" on the ocean"
# print(text.casefold())
# print(text.count("the"))
# print(text.endswith("ocean"))

fruit="apples"
txt= f"I love {fruit.upper()}"
print(txt)
