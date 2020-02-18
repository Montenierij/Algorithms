######################################################
# Jacob Montenieri
# Introduction To Algorithms
# Lab 6
# This lab goes over implementing BFS into graphs
# with unit distances.
######################################################
class Graph:

    def __init__(self):
        self.graph_dict = {}

    def addEdge(self, node, neighbour):
        if neighbour not in self.graph_dict.keys():
            self.graph_dict[neighbour] = []
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbour]
        else:
            self.graph_dict[node].append(neighbour)

    def show_edges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print("(", node, ", ", neighbour, ")")

    def explore(self, v):
        visited[v] = True
        for u in self.graph_dict[v]:                    #FOR EACH EDGE (v,u) CODE
            if not visited[u]:
                self.explore(u)
        post.append(v)

    def exploreprint(self, v):
        visited[v] = True
        getnum[-1].append(v)
        for u in self.graph_dict[v]:
            if not visited[u]:
                self.exploreprint(u)



    def dfs(self):
        for v in self.graph_dict.keys():
            visited[v] = False
        for v in self.graph_dict.keys():
            if not visited[v]:
                self.explore(v)

    def bfs(self, s):
        visited1 = [False] * (len(self.graph_dict))
        queue.append(s)
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for v in self.graph_dict[s]:  # FOR EACH EDGE (u,v) CODE
                if not visited1[v]:
                    queue.append(v)
                    visited1[v] = True
                    gr.addEdge(s, v) #HOW DO I PRINT LAST EDGE



prev = []
queue = []
dist = []
post = []
g = Graph()
gr = Graph()
counter = 0
visited = {}
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(0, 4)
g.addEdge(0, 5)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(4, 5)
g.bfs(0)
print('\n')
gr.show_edges()


#gr.dfs()
#for j in post:
#    visited[j] = False
#getnum = []
#while post:
#    s = post.pop()
#    if not visited[s]:
#        getnum.append([])
#        g.exploreprint(s)
#print(getnum)

