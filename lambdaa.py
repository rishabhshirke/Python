def func1(n):
    return lambda a : a*n


multiplier=func1(3)
print(multiplier(11))

s1 = 'GeeksforGeeks'

s2 = lambda x: x.upper()
print(s2(s1))

x=lambda a: "Positive" if a>0 else "Negative" if a<0 else "Zero"

print(x(2))
print(x(-2))


list1=[1,2,3,4,5,6,7,8,9]

x=filter(lambda a : a%2 ==0,list1)
print(list(x))