######################################################
# Jacob Montenieri
# Introduction To Algorithms
# Lab 9
# This lab goes over if a graph is bipartite or not.
# This is determined by seeing if vertices can be
# colored blue and red without having adjacent
# matching colors.
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



    def bipartite(self):
        for v in self.graph_dict.keys():
            visited[v] = ""
        queue = [0]
        visited[0] = "Red"
        while queue:
            s = queue.pop(0)
            for i in self.graph_dict[s]:
                if visited[i] == "":
                    queue.append(i)
                if visited[i] == visited[s]:
                    return False
                if visited[s] == "Red":
                    visited[i] = "Blue"
                elif visited[s] == "Blue":
                    visited[i] = "Red"
        return True


g = Graph()
visited = {}
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(2, 3)
g.addEdge(1, 0)
g.addEdge(2, 0)
g.addEdge(3, 1)
g.addEdge(3, 2)
if g.bipartite():
    print("Graph is bipartite")
else:
    print("Graph is not bipartite")
