class WeightedGraph:
    def __init__(self):
        self.graph ={}
        
    def add(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]={}
            
    def add_edge(self,from_vertex, to_vertex,weight,isDirected=False):
        self.add(from_vertex)
        self.add(to_vertex)
        self.graph[from_vertex][to_vertex]=weight
        if isDirected==False:
            self.graph[to_vertex][from_vertex]=weight
            
    def remove_edge(self,from_vertex,to_vertex):
        if from_vertex in self.graph and to_vertex in self.graph[from_vertex]:
            del self.graph[from_vertex][to_vertex]
        if to_vertex in self.graph and from_vertex in self.graph[to_vertex]:
            del self.graph[to_vertex][from_vertex]
            
    def remove_vertex(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]
        for vertex_in in self.graph:
            if vertex in self.graph[vertex_in]:
                del self.graph[vertex_in][vertex]
                
            
            
witheightedGraph=WeightedGraph()
witheightedGraph.add_edge("cheenai","bangalore",300)
#witheightedGraph.add("cheenai")
#witheightedGraph.add("bengalore")
print(witheightedGraph.graph)
witheightedGraph.remove_edge("cheenai","bangalore")
print(witheightedGraph.graph)
