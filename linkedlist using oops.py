class Node():
    def __init__ (self,data):
        self.data=data
        self.pointer= None
class Linkedlist:
    def __init__(self):
        self.head=None
    def add(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            cur=self.head
            while (cur.pointer is not None):
                cur=cur.pointer
            cur.pointer=newNode
    def print(self):
        c=self.head
        while c is not None:
            print(c.data ,end="  ")
            c=c.pointer
        print()
    def remove(self,data):
        if (self.head is not None):
            if(self.head.data==data):
                self.head=self.head.pointer
            else:
                cur=self.head
                while (cur.pointer is not None and cur.pointer.data!=data):
                    cur=cur.pointer
                if cur.pointer is not None:
                    cur.pointer=cur.pointer.pointer
                else:
                    print(data,"the data is not present in the linked list")

        else:
            print("empty")
        
            
        
                
                
            

        
l=Linkedlist()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.print()
l.remove(3)
l.print()
