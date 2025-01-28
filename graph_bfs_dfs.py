class Graph:
    def __init__(self):
        self.graph={}
    def AddVertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
        else:
            print("vertex already exists")
    def AddEdge(self,vertex1,vertex2,isDirected=False):
        self.AddVertex(vertex1)
        self.AddVertex(vertex2)
        self.graph[vertex1].append(vertex2)
        if not isDirected:
            self.graph[vertex2].append(vertex1)
    def Display(self):
        for key,value in self.graph.items():
            print(f"{key}==>{value}")
    def GetVertices(self):
        for i in self.graph:
            print(i)
    
    def GetEdges(self):
        for key,value in self.graph.items():
            for vertex in value:
                print(f"({key},{vertex})")
    def RemoveVertex(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            
            for key,value in self.graph.items():
                        if vertex in value:
                            value.remove(vertex)
    def IsEdge(self,vertex1,vertex2):
        return vertex1 in self.graph[vertex2] or  vertex2 in self.graph[vertex1] 
        
    def RemoveEdges(self,vertex1,vertex2):
        if self.IsEdge(vertex1,vertex2):
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)
    def Dfs(self,start,AlreadyVisited=set()):
        if start not in AlreadyVisited:
            AlreadyVisited.add(start)
            print(start,end=" ")
            
            for child in self.graph[start]:
                self.Dfs(child,AlreadyVisited)
    def Bfs(self,start):
        AlreadyVisited={start}
        Queue=[start]
        
        while len(Queue)>0:
            current=Queue.pop(0)
            print(current,end=" ")
            
            for child in self.graph[current]:
                if child not in AlreadyVisited:
                    Queue.append(child)
                    AlreadyVisited.add(child)
    
    def Shortestpath(self,start,end):
        AlreadyVisited={start}
        Queue=[(start,[start])]
        
        while len(Queue)>0:
            current,path =Queue.pop(0)
            print(current,end=" ")
            
            for child in self.graph[current]:
                if child== end:
                    return path+[child ]
                    
                if child not in AlreadyVisited:
                    Queue.append((child,path+[child]))
                    AlreadyVisited.add(child)
    
        
        
        
        
        
        
GRAPG1=Graph()
#GRAPG1.AddVertex('A')
#GRAPG1.AddVertex('B')
GRAPG1.AddEdge('A','B')
GRAPG1.AddEdge('B','C')
GRAPG1.AddEdge('B','D')
GRAPG1.AddEdge('C','D')
GRAPG1.Display()
GRAPG1.GetVertices()
GRAPG1.GetEdges()
#GRAPG1.RemoveVertex('C')
#GRAPG1.RemoveEdges('A','B')
GRAPG1.Display()
GRAPG1.Dfs('A')
print()
GRAPG1.Bfs('A')
print()
GRAPG1.Shortestpath('A','D')
