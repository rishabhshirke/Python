from doctest import testmod 

# def factorial(n): 
#     ''' 
#     This function calculates recursively and 
#     returns the factorial of a positive number. 
#     Define input and expected output: 
#     >>> factorial(3) 
#     6
#     >>> factorial(5) 
#     120
#     '''
#     if n <= 1: 
#         return 1
#     return n * factorial(n - 1) 

# if __name__ == '__main__': 
#     testmod(name ='factorial', verbose = True)



def add(a,b):
    '''
    >>> add(5,6)
    11
    '''

    return a+b


if __name__ == '__main__':
    testmod(name='add',verbose=True)