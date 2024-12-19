
#A Python decorator is a function that 
#takes in a function and returns it by adding some functionality.

# def add(func):
#     def value():
#         print("Executed")

#         func()
#     return value

# @add
# def print_message():#decorated function
#     print("Hello World")

# print_message()
# def smart_divide(func):
#     def wrapper(a,b):
#         print("Dividing")
#         if b == 0:
#             print("Error: Division by zero")
#             return
#         return func(a, b)
#     return wrapper

# @smart_divide
# def divide(a, b):
#     print(a/b)
# divide(2,0)


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def say_hi():
   return "Hello"

print(say_hi())


