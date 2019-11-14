
#!/usr/bin/env python

# Note: Not optimal nor the prettiest
# Based on pseudocode from CLRS book.

# run: 'python3 bellman-ford.py'

def bellmanFord(graph, source):
    initializeSingleSource(graph.verticies, source)
    for i in range(1, len(graph.verticies)):
        # The following two nested loops represent pseudocode: for each edge u,v in graph
        for (k, v) in graph.verticies.items():
            for edge in v.edges:
                relax(graph.verticies[edge.source], graph.verticies[edge.destination], edge.weight)
    # The following two nested loops represent pseudocode: for each edge u,v in graph
    for (k, v) in graph.verticies.items():
        for edge in v.edges:
            if graph.verticies[edge.source].cost > graph.verticies[edge.destination].cost + edge.weight:
                return False
    return True

def relax(currentVertex, destinationVertex, edgeWeight):
    if destinationVertex.cost > currentVertex.cost + edgeWeight:
        destinationVertex.cost = currentVertex.cost + edgeWeight
        destinationVertex.parent = currentVertex.selfIndex

def initializeSingleSource(verticies, source):
    # Already mostly initialized via Vertex constructor
    verticies[source].cost = 0

def printPath(graph, destination):
    path = []
    currIndex = destination
    path.append(destination)
    while graph[currIndex].parent != None:
        path.append(graph[currIndex].parent)
        currIndex = graph[currIndex].parent
    path.reverse()
    print('Path: ' + str(path))
    return path

class Graph:
    def __init__(self):
        self.verticies = {}

    def addVertex(self, vertex):
        self.verticies[vertex.selfIndex] = vertex

class Vertex:
    def __init__(self, selfIndex):
        self.selfIndex = selfIndex
        self.edges = []
        self.cost = float('Inf')
        self.parent = None
    
    def addEdge(self, edge):
        self.edges.append(edge)

class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

if __name__ == '__main__':
    # create graph
    graph = Graph()

    for i in range(1, 7):
        graph.addVertex(Vertex(i))

    edges = []
    edges.append(Edge(1, 4, 9))
    edges.append(Edge(1, 2, 3))
    edges.append(Edge(2, 5, 4))
    edges.append(Edge(2, 3, 4))
    edges.append(Edge(5, 4, 1))
    edges.append(Edge(5, 6, 4))

    for edge in edges:
        graph.verticies[edge.source].addEdge(edge)

    # decide source
    source = 1

    # decide destination
    destination = 4

    # run dijkstra on the graph
    bellmanFord(graph, source)

    # pluck out the minimum cost traversal
    print('Minimum cost: ' + str(graph.verticies[destination].cost))
    path = printPath(graph.verticies, destination)

    # basic test
    if path != [1, 2, 5, 4]:
        raise Exception