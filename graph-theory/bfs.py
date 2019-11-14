#!/usr/bin/env python

import math
import os
import random
import re
import sys

# n: number of nodes
# m: number of edges
# edges: 2D array of start and end nodes for edges
# s is our source (origin)

# return a list with lengths to each node from s, -1 if not accessible

# question uses 1-based indexes
# using 0-based during implementation

# basing this implementation on the pseudo code suggestion in CLRS

def bfs(n, m, edges, s):
    # initialization
    graph = {}
    verticies = [Vertice('zeroPlaceholder', -1, -1)]
    for i in range(1, n+1):
        verticies.append(Vertice('white', -1, i))
        graph[i] = []

    # create graph representation
    for edge in edges:
        edgeFrom = edge[0]
        graph[edgeFrom].append(edge[1])
        graph[edge[1]].append(edgeFrom) # remove if directed
    
    verticies[s].color = 'gray'
    verticies[s].distance = 0
    verticies[s].parent = None

    queue = [verticies[s]]

    # BFS, paiting according to:
    # white: unvisited
    # gray: visited
    # black: visited AND all edges from it are visited
    # Really only need 2 colors, or a 1/0 bit to distinguish states
    # keeping colors to fit CLRS model for easy explainability

    # BFS
    while len(queue) != 0:
        u = queue.pop(0)
        for v in graph[u.selfNum]:
            if verticies[v].color == 'white':
                verticies[v].color = 'gray'
                verticies[v].distance = u.distance + 1
                verticies[v].parent = u.selfNum
                queue.append(verticies[v])
        u.color = 'black'

    lengths = []
    for i in range(0, n+1):
        if i != s:
            vertex = verticies[i]
            distance = vertex.distance
            if distance != -1:
                distance *= 6
            lengths.append(distance)

    return lengths

class Vertice:
    def __init__(self, color, distance, selfNum):
        self.color = color
        self.distance = distance
        self.selfNum = selfNum
        self.parent = None

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        nm = raw_input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in xrange(m):
            edges.append(map(int, raw_input().rstrip().split()))

        s = int(raw_input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
