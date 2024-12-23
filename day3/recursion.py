def fib(n):

    if (n == 0):
        return 0
    if (n == 1 or n == 2):
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))

n = 5

for i in range(0,n): 
    print(fib(i),end=" ")

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

print(fact(5))