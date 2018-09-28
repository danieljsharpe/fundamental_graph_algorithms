#Kruskal's algorithm to find a MST for a given connected, undirected and weighted graph represented as a list of weighted edges

from collections import defaultdict

class Kruskal:

    def __init__(self,vertices):
        self.V = vertices # no. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph

    # function to add edge to graph
    def addedge(self,u,v,w):
        i = len(self.graph)
        self.graph.update({i:[u,v,w]})

    def printsoln(self, mst):
        print "Minimum spanning tree:\nEdge\tWeight"
        for i in range(self.V - 1):
            print mst[i][0], "-", mst[i][1], "\t", mst[i][2]

    # utility function to find set of an element i (uses path compression)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # utility function to perform union operation of two sets x & y (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x) # root node of tree to which x belongs
        yroot = self.find(parent, y)
        # attach smaller rank tree under root of higher rank tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else: # if ranks are same, make one (xroot) as root and increment its rank by one
            parent[yroot] = xroot
            rank[xroot] += 1

    # main function to construct MST using Kruskal's algorithm
    def kruskalmst(self):
        mstset = [] # data structure to store MST
        i = 0 # index variable used for sorting edges
        e = 0 # index variable used to count number of edges added to mstset
        # sort edges in increasing order of weight cost
        sortedkeys = sorted(self.graph, key = lambda item: self.graph.get(item)[2])
        print "sorted keys:\n", sortedkeys
        parent = []; rank = []
        # initially nodes are in distinct subsets
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u,v,w = self.graph.get(sortedkeys[i]) # choose edge with minimum weight cost
            i += 1
            x = self.find(parent, u)
            y = self.find(parent,v)
            if x != y: # no cycle; add edge to MST set and perform union on parent nodes of respective trees
                e += 1
                mstset.append([u,v,w])
                self.union(parent, rank, x, y)
            else: # reject edge
                continue
        self.printsoln(mstset)

# driver program
g = Kruskal(4)
g.addedge(0,1,10)
g.addedge(0,2,6)
g.addedge(0,3,5)
g.addedge(1,3,15)
g.addedge(2,3,4)
print "unsorted graph:\n", g.graph

g.kruskalmst()
