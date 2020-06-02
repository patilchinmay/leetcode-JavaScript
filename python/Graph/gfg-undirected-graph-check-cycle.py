# Working with undirected graph
# https://www.geeksforgeeks.org/detect-cycle-undirected-graph/

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

    def checkCycleHelper(self, node, visited, parent):
        visited[node] = True
        # print("node = ", node, "visited = ", visited)
        for neighbour in self.graph[node]:
            if visited[neighbour] == False:
                if self.checkCycleHelper(neighbour, visited, node):
                    return True
            elif neighbour != parent:
                return True

        return False

    def checkCycle(self):
        visited = [False] * self.vertices
        
        for node in self.graph:
            # print("#node = ", node, "visited = ", visited)
            if visited[node] == False:
                if self.checkCycleHelper(node, visited, -1) == True:
                    return True
        
        return False

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

    if graph.checkCycle():
        print("The graph is cyclic")
    else:
        print("The graph is NOT cyclic")