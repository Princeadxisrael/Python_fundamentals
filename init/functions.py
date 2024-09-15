# # def my_func(name1, name2):
# #     print("hello " + name1)

# # my_func("Anne")
# # my_func("Dennis")
# # my_func("John")

# #Arbitary Arguments
# def my_function(*kids):
#     print("The eldest child is " + kids[0])

# my_function("Johnny", "matty", "lukas")

# #key arguments
# def my_family(child3, child2, child1):
#     print("The youngest childe is " + child3)

# my_family(child1="Jonnie", child2="Elsie", child3="hannington")

# def my_country(country="kenya"):
#     print("I am from " + country)

# my_country("Norway")
# my_country()

# def myfunc(food):
#     for x in food:
#         print(" the ingredients for making chipati are :" + x)

# chipati=["flour","eggs", "salt", "sugar", "oil"]

# myfunc(chipati)

def my_func(x):
    pass


def tri_recursion(k):
    if(k>0):
        result= k + tri_recursion(k-1)
        print(result)
    else:
        result=0
    return result

print("\n\nrecursion examples result")
tri_recursion(6)


#Decorators

def decorator(func):
    def wrapper():
        print("this func is about to be called")
        func()
        print("this function has been called")
    return wrapper

@decorator
def get_called():
    print("I am the function that is called")

get_called=decorator(get_called)

get_called()

#define a decorator
def hello(func):

    def inner1():
        print("before function execution")

        func()

        print("func has been executed")

    return inner1

def func_to_be_called():
    print("This lives inside the function")

func_to_be_called=hello(func_to_be_called)

func_to_be_called()
