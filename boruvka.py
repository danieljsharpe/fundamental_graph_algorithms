# Boruvka's algorithm to find the MST of a connected, undirected and weighted graph represented as a list of weighted edges

from collections import defaultdict

class Boruvka:

    def __init__(self, vertices):
        self.V = vertices # no. of vertices
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addedge(self, u, v, w):
        i = len(self.graph)
        self.graph.update({i:[u,v,w]})

    def printsoln(self, mstset):
        print "final MST:\nEdge\t\tWeight"
        for i in range(len(mstset)):
            print mstset[i][0], " - ", mstset[i][1], "\t", mstset[i][2]

    # utility function to find set of an element i (uses path compression)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    #utility function to perform union of two sets x & y (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        # Attach smaller rank tree under root of high rank tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else: # ranks are same, so choose xroot to be root of tree
            parent[yroot] = xroot
            rank[xroot] += 1

    # main function to construct MST using Boruvka's algorithm
    def boruvkamst(self):
        mstset = []
        parent = []; rank = [];
        cheapest = [] # array to store index of cheapest edge for subset
        numtrees = self.V # initially each node is its own tree
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
            cheapest = [-1]*self.V
        # Keep combining components until all nodes are members of a single component
        while numtrees > 1:
            # Update cheapest edges for each component
            for i in range(len(self.graph)): # loop over edges
                #Find components of two corners of current edge
                u,v,w = self.graph[i]
                set1 = self.find(parent, u)
                set2 = self.find(parent, v)
                if set1 != set2: # check if current edge weight is smaller than previous cheapest edge weight connecting sets 1 & 2:
                    if cheapest[set1] == -1 or cheapest[set1][2] > w:
                        cheapest[set1] = [u,v,w]
                    if cheapest[set2] == -1 or cheapest[set2][2] > w:
                        cheapest[set2] = [u,v,w]
                else: # vertices of current edge belong to same component
                    continue
            # add the cheapest edges for each component to the MST
            for node in range(self.V):
                if cheapest[node] != -1: # component with index 'node' exists
                    u,v,w = cheapest[node]
                    set1 = self.find(parent, u)
                    set2 = self.find(parent, v)
                if set1 != set2:
                    self.union(parent, rank, set1, set2)
                    mstset.append((u,v,w))
                    numtrees -= 1
            cheapest = [-1]*self.V # reset array of cheapest edges
        self.printsoln(mstset)

# Driver program
g = Boruvka(4)
g.addedge(0,1,10)
g.addedge(0,2,6)
g.addedge(0,3,5)
g.addedge(1,3,15)
g.addedge(2,3,4)
print g.graph

g.boruvkamst()
