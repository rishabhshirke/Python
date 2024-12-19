
stack = []
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)


print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
# print(stack.pop())

print('\nStack after elements are popped:')
print(stack)
stack=[]

stack.append('a')
print(stack)
from collections import deque

stack=deque()

stack.append('e')
stack.append('d')
stack.append('c')
stack.append('b')
stack.append('a')

print(stack)

stack.pop()

print(stack)