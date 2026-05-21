'''
How will you decide which to use ?
if a graph is complete or almost complete , we should use adjacency matrix
if the number of edges are few then we should follw adjacency list '''

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def addvertex(self,vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def addneighbor(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            return True
        return False
    
    def removeVertex(self,vertex):
        if vertex not in self.adjacency_list.keys():
            print("Vertex not found.")
            return False
        else:
            self.adjacency_list.pop(vertex)
            self.removeEgde(vertex)
            return True

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, " = " ,self.adjacency_list[vertex]) 

graph = Graph()
graph.addvertex("A")
graph.addvertex("B")
graph.addvertex("C")
graph.addvertex("D")
graph.addvertex("E")
graph.addneighbor("A","B")
graph.addneighbor("A","C")
graph.addneighbor("A","D")
graph.addneighbor("B","A")
graph.addneighbor("B","E")
graph.addneighbor("C","A")
graph.addneighbor("C","D")
graph.addneighbor("D","A")
graph.addneighbor("D","C")
graph.addneighbor("D","E")
graph.addneighbor("E","B")
graph.addneighbor("E","D")
graph.removeVertex("E")
graph.print_graph()

