from collections import deque
stack=deque([1,2,3,4])
print(stack)
print(type(stack))
# access
print(stack[-1])
# insert
stack.append(5)
print(stack)
stack.appendleft(5)
print(stack)
#deletion
stack.pop()
print(stack)

