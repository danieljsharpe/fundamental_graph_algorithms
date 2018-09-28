# Prim's algorithm to find the minimum spanning tree (MST) of an undirected graph given in weighted adjacency matrix representation

import sys
import random

class Prim():

    def __init__(self, vertices, source = None):
        self.V = vertices # no. of nodes in graph
        self.graph = [[0 for col in range(vertices)]
                     for row in range(vertices)]
        self.src = source
        if source is None:
            self.src = random.randint(0,self.V-1)

# Utility function to print the constructed MST
    def printmst(self, edge):
        print "Edge \t Weight"
        for i in range(self.V):
            print edge[i][0],"-",edge[i][1],"\t",self.graph[edge[i][0]][edge[i][1]]

# Utility function to return node with minimum cost value from the set of nodes not currently included in the MST
    def mincost(self, cost, forest):
        min = sys.maxint # initialise min value
        for v in range(self.V-1,-1,-1): # if edge weights are same, highest index node is selected
            if cost[v] < min and forest[v] == False:
                min = cost[v]
                min_idx = v
        return min_idx

# Function to construct MST using Prim's algorithm
    def primmst(self):
        print "source node:", self.src
        cost = [sys.maxint]*self.V # cheapest cost of a connection to vertex v
        cost[self.src] = 0 # ensure source node is chosen first
        forest = [False]*self.V # nodes included in tree (initially none)
        unconn = [True]*self.V # nodes not included in tree (initially all)
        edge = dict((i, [i, -2]) for i in range(self.V)) # points to the edge providing the cheapest connection (i.e. defines tree)
        edge[self.src][1] = -1 # indicates that source node is root of tree
        for i in range(self.V):
            u = self.mincost(cost, forest)
            forest[u] = True
            unconn[u] = False
            for v in range(self.V): # update cost value of vertices adjacent to current node, if applicable
                if self.graph[u][v] > 0 and forest[v] == False and \
                   cost[v] > self.graph[u][v]:
                       cost[v] = self.graph[u][v]
                       edge[v][1] = u
        self.printmst(edge)
            

# Driver program
g  = Prim(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
          ];
#g.graph = [ [0, 2, 0, 6, 0],
#            [2, 0, 3, 8, 5],
#            [0, 3, 0, 0, 7],
#            [6, 8, 0, 0, 9],
#            [0, 5, 7, 9, 0],
#           ]
g.primmst()
