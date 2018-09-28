#Union-find (disjoint set) algorithm to detect the presence of a cycle given an undirected graph
#naive implementation

from collections import defaultdict

class Uf_cycle:

    def __init__(self,vertices):
        self.V = vertices # no. of nodes
        self.graph = defaultdict(list) # default dictionary to store graph

    #function to add edge connecting nodes u & v to graph
    def addedge(self,u,v):
        self.graph[u].append(v)

    #a utility function to find the subset of an element i
    def find_parent(self,parent,i):
        #naive implementation of find()
        if parent[i] == -1:
            return i
        else:
            return self.find_parent(parent,parent[i])

    #a utility function to perform the union of two subsets
    def union(self,parent,x,y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        parent[x_set] = y_set

    #main function
    def iscyclic(self):
        parent = [-1]*(self.V) # initialise parent array with all nodes belonging to distinct subsets
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent,i)
                y = self.find_parent(parent,j)
                if x == y:
                    return True # cycle found
                self.union(parent,x,y)

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
