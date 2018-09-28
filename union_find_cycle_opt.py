#Union-find (disjoint set) algorithm to detect the presence of a cycle given an undirected graph
#Optimised algorithm implementing both union by rank and path compression methods

from collections import defaultdict

class Uf_cycle:

    def __init__(self,vertices):
        self.V = vertices # no. of nodes
        self.graph = defaultdict(list) # default dictionary to store graph

    #function to add edge connecting nodes u & v to graph
    def addedge(self,u,v):
        self.graph[u].append(v)

    #a utility function to find the subset of an element i, implementing path compression
    def find_parent(self,parent,i):
        if parent[i][0] != i:
            parent[i][0], parent = self.find_parent(parent,parent[i][0])
        return parent[i][0], parent

    #a utility function to perform the union of two subsets, implementing union by rank
    def union(self,parent,x,y):
        xroot, parent = self.find_parent(parent, x)
        yroot, parent = self.find_parent(parent, y)
        #attach smaller rank tree under root of high rank tree
        if parent[xroot][1] < parent[yroot][1]:
            parent[xroot][0] = yroot
        elif parent[xroot][1] > parent[yroot][1]:
            parent[yroot][0] = xroot
        else:
            parent[yroot][0] = xroot
            parent[xroot][1] += 1
        return parent
            
    #main function
    def iscyclic(self):
        parent = [[i,0] for i in range(self.V)] # initialise, all nodes in distinct subsets (i.e. parent is v for node v) with rank 0
        for i in self.graph:
            for j in self.graph[i]:
                x, parent = self.find_parent(parent,i)
                y, parent = self.find_parent(parent,j)
                if x == y:
                    return True # cycle found
                parent = self.union(parent,x,y)

#Driver program
g = Uf_cycle(5) # create nodes of graph
g.addedge(0,1) # add vertices
g.addedge(1,2)
g.addedge(2,3)
g.addedge(2,4)
g.addedge(3,4)

print g.graph

if g.iscyclic():
    print "graph contains cycle"
else:
    print "graph does not contain cycle"
