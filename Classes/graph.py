import networkx as nx

class Graph():
  def __init__(self):
    self.G = nx.Graph()

  def addEdge(self, u, v):
    self.G.add_edge(u, v)

  def fromAdjacencyMatrix(self, matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i+1, n):
            if matrix[i][j] == 1:
                self.addEdge(i, j)
  
  def isIsomorphic(self, otherGraph):
    return nx.is_isomorphic(self.G, otherGraph.G)
  
  @staticmethod
  def readAdjacencyMatrixFromFile(pathFile):
    with open(pathFile, 'r') as file:
        lines = file.readlines()
        matrix = [[int(value) for value in line.split()] for line in lines]
    return matrix