List=[1,2,3,4]
'''
print(id(List[0]))
print(id(List[1]))
'''
class Node():
    def __init__ (self,data):
        self.data=data
        self.pointer= None
#    def __str__(self):
  #      return "node class"
head=Node(1)
node2=Node(2)
node3=Node(3)
head.pointer=node2
node2.pointer=node3
print(head.data)
print(head.pointer)
print(node2)

# treverse:
cur= head
while ( cur is not None):
    print(cur.data)
    cur=cur.pointer


