# Works with directed and undirected graph
# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

from collections import defaultdict 

class Graph:
    def __init__(self,vertices):
        self.vertices  = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def printGraph(self):
        for node in self.graph:
            print(node, "=" ,self.graph[node])

    def dfsHelper(self, node, visited):
        visited[node] = True
        print(node)

        for neighbour in self.graph[node]:
            if visited[neighbour] == False:
                self.dfsHelper(neighbour, visited)

    def dfs(self, node):
        visited = [False] * self.vertices
        self.dfsHelper(node, visited)

if __name__ == "__main__":
    # graph = Graph(7)
    # graph.addEdge(0,1)
    # graph.addEdge(0,2)
    # graph.addEdge(1,3)
    # graph.addEdge(1,4)
    # graph.addEdge(2,5)
    # graph.addEdge(2,6)

    graph = Graph(4)
    graph.addEdge(0,1)
    graph.addEdge(1,2)
    graph.addEdge(2,3)
    graph.addEdge(3,0)

    graph.printGraph()
    
    graph.dfs(0)