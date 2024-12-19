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