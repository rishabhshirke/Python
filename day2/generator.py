
def gen_func(n):
    value=0

    while(value<n):
        yield value #yield is used to produce value from generator function
        value+=1

# g=gen_func(3)
# print(next(g))
for i in gen_func(5):
    print(i)


#Generator Expressions
#produces the values of expression for each item in the 
#iterable, one at a time, when iterated over.

# list1=[1,2,3,4,5,6]

# x=(x for x in list1)
# for i in x:
#     print(i)

x=(x for x in range(100) if x % 2 ==0)
for i in x:
    print(i)

def multiple_yield():  
    str1 = "First String"  
    yield str1  
      
    str2 = "Second string"  
    yield str2  
      
    str3 = "Third String"  
    yield str3  
obj = multiple_yield()  
print(next(obj))  
print(next(obj))  
print(next(obj))  