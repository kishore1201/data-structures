#min heap
class HeapNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class MinHeap:
    def __init__(self):
        self.root=None
        
    def add(self,data):
        
        if not self.root:
            self.root = HeapNode(data)
            return
        self.rec_add(data,self.root)

    def rec_add(self,data,node):
        if not node.left:
            node.left = HeapNode(data)
            self.heapify_up(node.left)
        elif not node.right:
            node.right=HeapNode(data)
            self.heapify_up(node.right)
        else:
            if self.getcount(node.left)<=self.getcount(node.right):
                self.rec_add(data,node.left)
            else:
                self.rec_add(data,node.right)
            
    def  getcount(self,node):
        if not node:
            return 0
        
        return 1+self.getcount(node.left)+self.getcount(node.right)
            
    def heapify_up(self,node):
        while node and node !=self.root:
            parent = self.getParent(node,self.root)
            if parent.data>node.data:
                parent.data,node.data=node.data,parent.data
                node=parent
            else:
                break
            
            
    def get_parent(self,node,root):
        if root.left==node or root .right ==node:
            return root
        if root.left:
            parent=self.get_parent(node,root.left)
            if parent:return parent
            
  
  
  
  
  
            
heap=HeapNode()
heap.add(10)
heap.add(7)
heap.add(6)
heap.add(5)
heap.add(4)