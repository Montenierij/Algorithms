###########################################################
# Jacob Montenieri
# Introduction To Algorithms
# Lab 5
# This lab implements the linear time strongly connected
# components algorithm and takes a given graph and creates
# the reversed graph in linear time. After this, the
# program runs an undirected connected components method
# that processes in post order
###########################################################
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
        for u in self.graph_dict[v]:
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


file1 = open(r"EXAMPLE.txt")
post = []
g = Graph()
gr = Graph()
counter = 0
visited = {}


while True:
    y = file1.readline()
    if y == "":
        break
    y = y.splitlines()
    x = y[0].split(" ")
    g.addEdge(x[0], x[1])
    gr.addEdge(x[1], x[0])
gr.dfs()
for j in post:
    visited[j] = False
getnum = []
while post:
    s = post.pop()
    if not visited[s]:
        getnum.append([])
        g.exploreprint(s)

print(getnum)

