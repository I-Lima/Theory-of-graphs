class Graph():
	def __init__(self):
		self.adjMatrix = None

	def setAdjacencyMatrix(self, adjMatrix):
		self.adjMatrix = adjMatrix

	def isIsomorphic(self, otherGraph):
		# Check if the graphs have the same number of vertices
		if len(self.adjMatrix) != len(otherGraph.adjMatrix):
				return False

		# Check if the number of edges is equal
		def edge_count(matrix):
				count = 0
				for row in matrix:
						count += sum(row)
				return count

		if edge_count(self.adjMatrix) != edge_count(otherGraph.adjMatrix):
				return False
		
		n = len(self.adjMatrix)
		
		# Check if the degree of each vertex is preserved
		def checkDegrees(matrix):
				degrees = [sum(row) for row in matrix]
				return sorted(degrees)

		if checkDegrees(self.adjMatrix) != checkDegrees(otherGraph.adjMatrix):
				return False

		# Define a function to check if the graph structure is preserved under a bijection
		def isomorphicCheck(mapping):
				mappedGraph = [[0] * n for _ in range(n)]

				for i in range(n):
						for j in range(n):
								if self.adjMatrix[i][j] == 1:
										mappedGraph[mapping[i]][mapping[j]] = 1

				return mappedGraph

		# Generate all possible permutations of the vertices of the current graph
		def generateMappings(mapping, index):
				if index == n:
						mappedGraph = isomorphicCheck(mapping)
						if mappedGraph == otherGraph.adjMatrix:
								return True
						return False

				for i in range(n):
						if i not in mapping[:index]:
								mapping[index] = i
								if generateMappings(mapping, index + 1):
										return True

				return False

		return generateMappings([0] * n, 0)
	
	@staticmethod
	def readAdjacencyMatrixFromFile(pathFile):
		with open(pathFile, 'r') as file:
			lines = file.readlines()
			matrix = [[int(value) for value in line.split()] for line in lines]
		return matrix
	
	def isSimilar (self, otherGraph, type):
		maxIterations = 100
		tolerance = 1e-4
		C = 0.75
		adjMatrix2 = otherGraph.adjMatrix

		def dotProduct(vector1, vector2):
				return sum(x * y for x, y in zip(vector1, vector2))

		def norm(vector):
				return sum(x ** 2 for x in vector) ** 0.5

		if type == 'cosine':
				# Converting the adjacency matrix into a vecto
				vector1 = [val for row in self.adjMatrix for val in row]
				vector2 = [val for row in adjMatrix2 for val in row]

				# Calculating the inner product
				dotProd = dotProduct(vector1, vector2)

				# Calculating the norm of the vectors
				normVector1 = norm(vector1)
				normVector2 = norm(vector2)

				# Calculating the cosine similarity
				if normVector1 == 0 or normVector2 == 0:
						return 0  # Avoid division by zero
				similarity = dotProd / (normVector1 * normVector2)
				return similarity
		elif type == 'simRank':
				n = len(self.adjMatrix)

				# Initialize the similarity matrix
				simMatrix = [[0] * n for _ in range(n)]
				for i in range(n):
						simMatrix[i][i] = 1

				# Convergence of the SimRank algorithm
				for iteration in range(maxIterations):
						prevSimMatrix = [row[:] for row in simMatrix]

						# Calculate the similarity for each pair of vertices
						for i in range(n):
								for j in range(n):
										if i != j:
												sumSim = 0
												neighborsI = [idx for idx, val in enumerate(self.adjMatrix[i]) if val == 1]
												neighborsJ = [idx for idx, val in enumerate(adjMatrix2[j]) if val == 1]

												for u in neighborsI:
														for v in neighborsJ:
																sumSim += prevSimMatrix[u][v]

												simMatrix[i][j] = C / (len(neighborsI) * len(neighborsJ)) * sumSim

						# Check for convergence
						converged = True
						for i in range(n):
								for j in range(n):
										if abs(simMatrix[i][j] - prevSimMatrix[i][j]) > tolerance:
												converged = False
												break

						if converged:
								break

				total_sim = sum(sum(row) for row in simMatrix)
				max_possible_sim = n * (n - 1)
				similarity = total_sim / max_possible_sim if max_possible_sim != 0 else 0

				return similarity
		elif type == 'jaccard':
				# Number of vertices in each graph
				n = len(self.adjMatrix)

				# Calculate the Jaccard similarity for each pair of vertices
				similarities = []
				for i in range(n):
						neighbors1 = set(j for j, val in enumerate(self.adjMatrix[i]) if val == 1)
						neighbors2 = set(j for j, val in enumerate(adjMatrix2[i]) if val == 1)
						intersection = len(neighbors1.intersection(neighbors2))
						union = len(neighbors1.union(neighbors2))
						similarity = intersection / union if union != 0 else 0  # Avoid division by zero
						similarities.append(similarity)

				# Calculate the average similarity between the vertices
				averageSimilarity = sum(similarities) / n
				return averageSimilarity
		else:
				return None
