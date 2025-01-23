# stack
stack=[1,2,3,4]
#accesing
print(stack[-1])

#stack overflow--> excess data insertion error while the size is fixed
#stack underflow--> an empty stack to access
'''a=[]
print(a[-1])'''
# insertion
stack.append(5)# it s also like push
print(stack[-1])

#deletion
stack.pop()
print(stack[-1])
#search
x=4
if x==stack[-1]:
    print("true")
