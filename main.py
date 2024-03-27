from Classes import graph
from Classes import utils
Graph = graph.Graph()
Utils = utils.Utils()

file1, file2 = Utils.readGraphs()
similarityMethod = Utils.readSimilarityMethod()

graph1 = graph.Graph()
graph2 = graph.Graph()

graph1.setAdjacencyMatrix(Graph.readAdjacencyMatrixFromFile(file1))
graph2.setAdjacencyMatrix(Graph.readAdjacencyMatrixFromFile(file2))

print("----------------------------------------------------------------------------------------")

print("The adjacency matrices of the graphs are:")

print("Graph 1", graph1.adjMatrix)
print("Graph 2", graph2.adjMatrix)

similarity = graph1.isSimilar(graph2, similarityMethod)

message = "The graphs "
if graph1.isIsomorphic(graph2):
    message = message + ("are isomorphic and")
else:
    message = message +  ("are not isomorphic and")

if  similarity > 0.75:
    message = message + (" are similar.")
else:
    message = message + (" are not similar.")

print("Have a similarity of:", similarity, "using the method", similarityMethod)
print(message)
print("----------------------------------------------------------------------------------------")