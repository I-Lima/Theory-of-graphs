from Classes import graph
from Classes import utils
Graph = graph.Graph()
Utils = utils.Utils()

graph1 = graph.Graph()
graph2 = graph.Graph()

graph1.setAdjacencyMatrix(Graph.readAdjacencyMatrixFromFile('Files/graph1.txt'))
graph2.setAdjacencyMatrix(Graph.readAdjacencyMatrixFromFile('Files/graph2.txt'))

print("----------------------------------------------------------------------------------------")

print("The adjacency matrices of the graphs are:")

print("Graph 1", graph1.adjMatrix)
print("Graph 2", graph2.adjMatrix)

similarityCosine = graph1.isSimilar(graph2, 'cosine')
similaritySimRank = graph1.isSimilar(graph2, 'simRank')
similarityJaccard = graph1.isSimilar(graph2, 'jaccard')

message = "The graphs "
if graph1.isIsomorphic(graph2):
    message = message + ("are isomorphic and")
else:
    message = message +  ("are not isomorphic and")

if  similarityCosine > 0.75:
    message = message + (" are similar.")
else:
    message = message + (" are not similar.")

print("Have a similarity of:", similarityCosine, "using the method cosine")
print("Have a similarity of:", similaritySimRank, "using the method simRank")
print("Have a similarity of:", similarityJaccard, "using the method jaccard")
print(message)
print("----------------------------------------------------------------------------------------")

print(" ")
print(" ")
print(" ")

graph1.setAdjacencyMatrix(Graph.readAdjacencyMatrixFromFile('Files/graph3.txt'))
graph2.setAdjacencyMatrix(Graph.readAdjacencyMatrixFromFile('Files/graph4.txt'))

print("----------------------------------------------------------------------------------------")

print("The adjacency matrices of the graphs are:")

print("Graph 4", graph1.adjMatrix)
print("Graph 5", graph2.adjMatrix)

similarityCosine = graph1.isSimilar(graph2, 'cosine')
similaritySimRank = graph1.isSimilar(graph2, 'simRank')
similarityJaccard = graph1.isSimilar(graph2, 'jaccard')

message = "The graphs "
if graph1.isIsomorphic(graph2):
    message = message + ("are isomorphic and")
else:
    message = message +  ("are not isomorphic and")

if  similarityCosine > 0.75:
    message = message + (" are similar.")
else:
    message = message + (" are not similar.")

print("Have a similarity of:", similarityCosine, "using the method cosine")
print("Have a similarity of:", similaritySimRank, "using the method simRank")
print("Have a similarity of:", similarityJaccard, "using the method jaccard")
print(message)
print("----------------------------------------------------------------------------------------")

print(" ")
print(" ")
print(" ")

graph1.setAdjacencyMatrix(Graph.readAdjacencyMatrixFromFile('Files/graph5.txt'))
graph2.setAdjacencyMatrix(Graph.readAdjacencyMatrixFromFile('Files/graph6.txt'))

print("----------------------------------------------------------------------------------------")

print("The adjacency matrices of the graphs are:")

print("Graph 5", graph1.adjMatrix)
print("Graph 6", graph2.adjMatrix)

similarityCosine = graph1.isSimilar(graph2, 'cosine')
similaritySimRank = graph1.isSimilar(graph2, 'simRank')
similarityJaccard = graph1.isSimilar(graph2, 'jaccard')

message = "The graphs "
if graph1.isIsomorphic(graph2):
    message = message + ("are isomorphic and")
else:
    message = message +  ("are not isomorphic and")

if  similarityCosine > 0.75:
    message = message + (" are similar.")
else:
    message = message + (" are not similar.")

print("Have a similarity of:", similarityCosine, "using the method cosine")
print("Have a similarity of:", similaritySimRank, "using the method simRank")
print("Have a similarity of:", similarityJaccard, "using the method jaccard")
print(message)
print("----------------------------------------------------------------------------------------")

print(" ")
print(" ")
print(" ")

graph1.setAdjacencyMatrix(Graph.readAdjacencyMatrixFromFile('Files/graph7.txt'))
graph2.setAdjacencyMatrix(Graph.readAdjacencyMatrixFromFile('Files/graph8.txt'))

print("----------------------------------------------------------------------------------------")

print("The adjacency matrices of the graphs are:")

print("Graph 7", graph1.adjMatrix)
print("Graph 8", graph2.adjMatrix)

similarityCosine = graph1.isSimilar(graph2, 'cosine')
similaritySimRank = graph1.isSimilar(graph2, 'simRank')
similarityJaccard = graph1.isSimilar(graph2, 'jaccard')

message = "The graphs "
if graph1.isIsomorphic(graph2):
    message = message + ("are isomorphic and")
else:
    message = message +  ("are not isomorphic and")

if  similarityCosine > 0.75:
    message = message + (" are similar.")
else:
    message = message + (" are not similar.")

print("Have a similarity of:", similarityCosine, "using the method cosine")
print("Have a similarity of:", similaritySimRank, "using the method simRank")
print("Have a similarity of:", similarityJaccard, "using the method jaccard")
print(message)
print("----------------------------------------------------------------------------------------")
