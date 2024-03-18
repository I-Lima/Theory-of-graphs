from Classes import graph
from Classes import utils
Graph = graph.Graph()
Utils = utils.Utils()

file1, file2 = Utils.readGraphs()

graph1 = graph.Graph()
graph2 = graph.Graph()

graph1.fromAdjacencyMatrix(Graph.readAdjacencyMatrixFromFile('Files/graph1.txt'))
graph2.fromAdjacencyMatrix(Graph.readAdjacencyMatrixFromFile('Files/graph2.txt'))


if graph1.isIsomorphic(graph2):
    print("Os grafos são isomorfos.")
else:
    print("Os grafos não são isomorfos.")