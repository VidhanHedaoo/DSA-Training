# adjacency matrix is a 2d matrix used to represent the graph
# A---------B
# |         |
# |         |
# |         |
# C---------D

# connection:         
# A <-> B
# A <-> C
# B <-> D
# C <-> D

#  Matrix:
#    A  B  C  D
# A  0  1  1  0
# B  1  0  0  1
# C  1  0  0  1
# D  0  1  1  0

class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def display(self):
        print("Adjacency Matrix")
        for row in self.matrix:
            print(row)

    def addedge(self,u,v):
        self.matrix[u][v]= 1    

    def removeedge(self,u,v):
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0


graph = Graph(4)

graph.addedge(0,1)
graph.addedge(0,2)
graph.addedge(1,0)
graph.addedge(1,3)
graph.addedge(2,0)
graph.addedge(2,3)
graph.addedge(3,1)
graph.addedge(3,2)
graph.removeedge(1,3)

graph.display()

''' Output->
Adjacency Matrix
[0, 1, 1, 0]
[1, 0, 0, 0]
[1, 0, 0, 1]
[0, 0, 1, 0]'''

