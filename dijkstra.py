import sys
import numpy as np

class Dijkstra():

    def __init__(self,vertices,target=None):
        self.V = vertices
        self.graph = [[0 for col in range(vertices)]
                      for row in range(vertices)]
        self.tgt = target

    def printpathtotarget(self, spseq):
        print "Shortest path sequence (target -> source); "
        u = self.tgt
        while spseq[u][0] != -1:
            v = spseq[u][0]
            print u, "\t", spseq[v][1], "\t", v
            u = spseq[u][0]
        return

    def printsoln(self, dist, tree):
        print "Shortest path tree, distances:"
        for node in range(self.V):
            print node, "\t", dist[node]
        print "Shortest path tree; connectivity (child/parent)"
        for node in range(self.V):
            print node, "\t", tree[node]
        return

    # Function to read shortest path from source to target node by reverse iteration
    def retracepath(self, tree, dist):
        cumdist = 0 # cumulative distance
        v = self.tgt
        u = tree[self.tgt]
        spseq = {self.tgt: (u, 0)} # shortest path between source and target nodes (item is child node (-1 if N/A) / cumulative distance)
        while tree[u] != -1:
            cumdist += self.graph[u][v]
            spseq[u] = tree[u], cumdist
            v = u
            u = tree[u]
        cumdist += self.graph[u][v]
        spseq[u] = -1, cumdist
        return spseq

    # A utility function to find the minimum distance vertex from the set of
    # vertices not yet included in the SPT set
    def mindistance(self,dist,sptset):
        minim = sys.maxint # initialise min distance for next node
        # search for nearest vertex not in the SPT
        for v in range(self.V):
            if dist[v] < minim and sptset[v] == False:
                minim = dist[v]
                u = v # set next current minimum
        return u

    # Function that implements Dijkstra's shortest path algorithm to find the
    # shortest path tree (SPT) given the single source node src
    def dijkstraspt(self, src):
        dist = [sys.maxint]*self.V # initialise distances to infinity...
        dist[src] = 0 # ...except for chosen source node, defined as index zero
        sptset = [False]*self.V
        tree = dict((i, -1) for i in range(self.V)) # shortest path tree connectivity (-1 means no parent node)
        for i in range(self.V):
            u = self.mindistance(dist,sptset)
            sptset[u] = True
            if self.tgt is not None and u == self.tgt:
                spseq = self.retracepath(tree, dist)
                self.printpathtotarget(spseq)
                return
            for v in range(self.V): # update distances
                if self.graph[u][v] > 0 and sptset[v] == False and \
                   dist[v] > dist[u] + self.graph[u][v]:
                       dist[v] = dist[u] + self.graph[u][v]
                       tree[v] = (u)
        self.printsoln(dist, tree)

#a random graph (crude method)
#d = 15 # max distance
#n = 10 #nodes in graph
#g = np.random.randint(0,d,(n,n))

#Driver program
g = Dijkstra(9,4)
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
g.dijkstraspt(0)
