[Leia esta página em português](README.md)

# Graph Theory

## Table of Contents

- [Graph Theory](#graph-theory)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Running the Project](#running-the-project)
  - [Graph Class](#graph-class)
    - [Methods](#methods)
    - [Isomorphism Verification](#isomorphism-verification)
    - [Similarity Check](#similarity-check)
  - [Utils Class](#utils-class)
    - [Methods](#methods-1)
  - [Test Cases](#test-cases)

## Description

This repository contains code developed for the Graph Theory course.

## Running the Project

To run the project, follow the steps below:

1. Ensure your environment is configured for Python.
2. Clone the repository: <https://github.com/I-Lima/Theory-of-graphs.git>.
3. Import the project into your preferred IDE.
4. Run the program with the following command:

```bash
python main.py
```

## Graph Class

The Graph class is a representation of an undirected graph. It contains methods for graph manipulation and for calculating different types of similarity between two graphs. Graph manipulation is done through the adjacency matrix.

### Methods

- **setAdjacencyMatrix**: Sets the adjacency matrix of the graph.
- **isIsomorphic**: Checks if two graphs are isomorphic, meaning they have the same basic structure.
- **readAdjacencyMatrixFromFile**: Reads an adjacency matrix from a file.
- **isSimilar**: Calculates the similarity between two graphs based on different metrics: cosine, SimRank, and Jaccard.

### Isomorphism Verification

The `isIsomorphic` method is responsible for verifying if two graphs are isomorphic. A graph is isomorphic to another if there is a bijective correspondence between their sets of vertices such that the graph structure (relationships between vertices) is preserved.

This method employs a straightforward and systematic approach to verify isomorphism between two graphs, ensuring that all necessary criteria for isomorphism are appropriately checked. It traverses each essential step to determine if the graphs are isomorphic and returns the appropriate result based on these criteria.

### Similarity Check

The `isSimilar` method is responsible for calculating the similarity between two graphs using different metrics: cosine, SimRank, and Jaccard. Each metric provides a perspective on the similarity between the graphs, considering different aspects of their structure and connectivity.

## Utils Class

The Utils class provides auxiliary methods for reading graphs and selecting the similarity calculation method between them. It allows the user to choose between manually inputting file paths or reading pre-saved files, as well as selecting the desired similarity method.

### Methods

- **readGraphs**: This method allows the user to select between manually inputting file paths containing the graphs or using pre-saved paths.
- **readSimilarityMethod**: This method allows the user to choose the method for calculating similarity between the graphs.

## Test Cases

The project includes some test cases that can be executed using the following command:

```bash
python testCases.py
```
