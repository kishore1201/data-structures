class TreeNOde:
    def __init__(self, value):
        self.value = value
        self.children = []
        
class Tree:
    def __init__(self, root):
        self.root = None
    
    def bfs (self, node):
        tobevisited=[node]
        while len(tobevisited)>0:
            visit=tobevisited.pop(0)
            
            print(visit.value)
            
            for child in visit.children:
                tobevisited.append(child)
        
        
tree=Tree()
node1=TreeNOde(1)
node2=TreeNOde(2)
node3=TreeNOde(3)
node4=TreeNOde(4)
node5=TreeNOde(5)
node6=TreeNOde(6)

tree.root=node1
node1.children=[node1,node2]
node2.children=[node4,node5,node6]
tree.bfs(node1)

