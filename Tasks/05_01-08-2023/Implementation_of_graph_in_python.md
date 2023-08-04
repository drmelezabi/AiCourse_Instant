## Implementation of graph in python

In Python, you can implement a graph using various data structures. Two commonly used data structures for graph representation are the **adjacency matrix** and the **adjacency list**. The choice of data structure depends on the type of operations you need to perform on the graph and the nature of the graph (sparse or dense).

Here's an explanation and implementation of both methods:

### Adjacency Matrix:

An adjacency matrix is a 2D matrix where the cells represent the presence or absence of edges between vertices. If the graph is unweighted, the cell value is typically 1 (for an edge) or 0 (for no edge). For a weighted graph, the cell value can be the weight of the edge.

**Pros**:

- Directly shows if there's an edge between any two vertices.
- Constant time access to check edge existence.

**Cons**:

- Memory inefficient for sparse graphs (when most of the cells are zero).

Implementation:

```python
class GraphAdjacencyMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, source, destination, weight=1):
        self.matrix[source][destination] = weight
        self.matrix[destination][source] = weight  # Uncomment this line for an undirected graph

    def remove_edge(self, source, destination):
        self.matrix[source][destination] = 0
        self.matrix[destination][source] = 0  # Uncomment this line for an undirected graph

    def has_edge(self, source, destination):
        return self.matrix[source][destination] != 0

    def get_weight(self, source, destination):
        return self.matrix[source][destination]

# Example usage:
graph = GraphAdjacencyMatrix(5)
graph.add_edge(0, 1, 3)
graph.add_edge(0, 2, 1)
graph.add_edge(2, 3, 5)

print(graph.has_edge(0, 1))  # Output: True
print(graph.get_weight(0, 2))  # Output: 1
```

### Adjacency List:

An adjacency list is a collection of lists or dictionaries, where each vertex has a list/dictionary containing its adjacent vertices.

**Pros**:

- Memory efficient for sparse graphs.
- Efficient for traversing the neighbors of a vertex.

**Cons**:

- Requires more time to check for the presence of an edge.

Implementation:

```python
class GraphAdjacencyList:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination, weight=1):
        if source not in self.graph:
            self.graph[source] = []
        self.graph[source].append((destination, weight))
        # Uncomment the following line for an undirected graph
        # if destination not in self.graph: self.graph[destination] = []; self.graph[destination].append((source, weight))

    def remove_edge(self, source, destination):
        if source in self.graph:
            self.graph[source] = [(dest, weight) for dest, weight in self.graph[source] if dest != destination]

        # Uncomment the following block for an undirected graph
        # if destination in self.graph:
        #     self.graph[destination] = [(src, weight) for src, weight in self.graph[destination] if src != source]

    def has_edge(self, source, destination):
        return destination in self.graph.get(source, [])

    def get_neighbors(self, vertex):
        return self.graph.get(vertex, [])

# Example usage:
graph = GraphAdjacencyList()
graph.add_edge(0, 1, 3)
graph.add_edge(0, 2, 1)
graph.add_edge(2, 3, 5)

print(graph.has_edge(0, 1))  # Output: True
print(graph.get_neighbors(0))  # Output: [(1, 3), (2, 1)]
```

Choose the appropriate representation based on your requirements and the characteristics of your graph. For most cases, an adjacency list is preferred, especially for large and sparse graphs.
