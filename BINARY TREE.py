class Node:
    def __init__(self, data):
        self.data = data
        self.left= None
        self.right=None

class BinaryTree:

    def __init__(self):
        self.root = None

    def add(self,data):
        if not self.root:
            self.root=Node(data)
            return

        self.recadd(data,self.root)

    def recadd(self,data,node):
        if node.left is None:
            node.left=Node(data)
        elif node.right is None:
            node.right=Node(data)
        else:
            self.recadd(data,node.left)

    def display(self,depth=0,node=None):
        if node is None:
            node=self.root
        print(" " *depth,node.data)

        if node.left is  not None:
            self.display(depth+1,node.left)

        if node.right is  not None:
            self.display(depth+1,node.right)

    def remove(self,data):
        if not self.root:
            print("the root is empty")
            return
        if self.root.data==data:
            self.root=None
            return
        self.recremove(data,self.root)

    def recremove( self,data,node):
            if node.left and node.left.data==data:
                node.left=None
                return
            if node.right and node.right.data==data:
                node.right=None
                return

            if node.left:
                self.recremove(data,node.left)

            if node.right:
                self.recremove(data,node.right)
    def search(self,data):
        nodefind=self.recsearch(data,self.root)
        if nodefind:
                print("true")
        else:
                print("false")
            

    def recsearch(self,data,node):
        if not node or node.data==data:
            return node
        
        return self.recsearch(data,node.left) or self.recsearch(data,node.right)

    



            
        
        

    
        
        

binary=BinaryTree()
binary.add(5)
binary.add(1)
binary.add(2)
binary.add(3)
binary.add(4)
binary.add(5)
binary.display()
binary.remove(4)
binary.display()
binary.search(6)
