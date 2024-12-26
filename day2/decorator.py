
def decorator_func(func):
    def wrapper():
        print("Hello")

        func()

    return wrapper

@decorator_func
def name():
    print("MY name is rishabh")

name()

def decorator(a,b,c):
    def inner(func):        
        def wrapper():
            r=a+b+c
        
            return r
        return wrapper
    return inner

@decorator(4,5,7)
def my_func():
    return 0
print(my_func())