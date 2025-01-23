class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left= None
        self.right=None
class BinarysearchTree:
    def __init__(self):
        self.root=None

    def add(self,data):
        if not self.root:
            self.root=BSTNode(data)
            return
        self.recadd(data,self.root)

    def recadd(self,data,node):
        if data<node.data:
            if not node.left:
                node.left=BSTNode(data)
            else:
                self.recadd(data,node.left)
                      
        elif data>node.data:
             if not node.right:
                node.right=BSTNode(data)
             else:
                self.recadd(data,node.right)
    def display(self):
        result=[]
        self.inordertraversal(self.root,result)
        print("inorder",result)
        result2=[]
        self.preordertraversal(self.root,result2)
        print("pre order",result2)
        result3=[]
        self.postordertraversal(self.root,result3)
        print("post order" ,result3)
        
    def inordertraversal(self,node,result):
        if not node:
            return None
        else:
            self.inordertraversal(node.left,result)
            result.append(node.data)
            self.inordertraversal(node.right,result)
    def preordertraversal(self,node,result):
        if not node:
            return None
        else:
            result.append(node.data)
            self.preordertraversal(node.left,result)
            self.preordertraversal(node.right,result)
    def postordertraversal(self,node,result):
        if not node:
            return None
        else:
            self.postordertraversal(node.left,result)
            self.postordertraversal(node.right,result)
            result.append(node.data)
    def remove(self,data):
        if  not self.root:
            print("tree is empty")
            return
        
        if self.root.data==data:
            self.root=None
            return
        self.recremove(self.root,data)

    def recremove(self,node,data):
        if node.left.data==data and node.left :
            node.left=None
            return
        elif node.right.data==data and node.right:
            node.right=None
            return
        elif data<node.data:
            self.recremove(node.left,data)
        elif data>node.data:
            self.recremove(node.right,data)

    def search(self,data):
        node=self.recsearch(self.root,data)
        if node:
            print("true")
        else:
            print("false")

    def recsearch(self,node,data):
        if not node:
            return None
        
        if node.data==data and node:
            return node
        elif data<node.data:
            return self.recsearch(node.left,data)
        elif  data>node.data:
            return self.recsearch(node.right,data)

        
        

        
            
        
        
    

bst=BinarysearchTree()
bst.add(45)
bst.add(10)
bst.add(50)
bst.add(9)
bst.add(11)
bst.add(51)
bst.add(46)
bst.display()
bst.remove(10)
bst.search(4564)

