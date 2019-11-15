#!/usr/bin/env python

# Note: Not optimal. (fib min-max heap may be better to minimize extractMin iterations)
# Based on pseucode from CLRS book
# Greedy algorithm (sort of a combo of BFS and Prim's algo)

# run: 'python3 dijkastras.py'

def dijkstra(graph, source, destination):
    initializeSingleSource(graph.verticies, source)
    queue = graph.verticies
    calcedVerticies = {}
    while len(queue) != 0:
        (key, u) = extractMin(queue) # greedy traversal strategy
        for edge in u.edges:
            if edge.destination in queue:
                relax(u, queue[edge.destination], edge.weight)
            else:
                relax(u, calcedVerticies[edge.destination], edge.weight)
        calcedVerticies[key] = queue.pop(key)
    return calcedVerticies
    
def relax(currentVertex, destinationVertex, edgeWeight):
    if destinationVertex.cost > currentVertex.cost + edgeWeight:
        destinationVertex.cost = currentVertex.cost + edgeWeight
        destinationVertex.parent = currentVertex.selfIndex

def initializeSingleSource(verticies, source):
    # Diff from CLRS: already mostly initialized via Vertex constructor
    verticies[source].cost = 0

def extractMin(queue):
    # change this parameter to a heap instead for better performance
    minVertex = Vertex(-1)
    key = -1
    for (k, vertex) in queue.items():
        if minVertex.cost >= vertex.cost:
            minVertex = vertex
            key = k
    return (key, minVertex)

def printPath(graph, destination):
    path = []
    currIndex = destination
    path.append(destination)
    while graph[currIndex].parent != None:
        path.append(graph[currIndex].parent);
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
    result = dijkstra(graph, source, destination)

    # pluck out the minimum cost traversal
    print('Minimum cost: ' + str(result[destination].cost))
    path = printPath(result, destination)

    # basic test
    if path != [1, 2, 5, 4]:
        raise Exception
