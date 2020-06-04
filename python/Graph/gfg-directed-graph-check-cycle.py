# Working with directed graph
# https://www.geeksforgeeks.org/detect-cycle-in-a-graph/

from collections import defaultdict 

class Graph:
    def __init__(self,vertices):
        self.vertices  = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        # self.graph[v].append(u) # Commented because this is a directed graph
    
    def printGraph(self):
        for node in self.graph:
            print(node, "=" ,self.graph[node])

    def checkCycleHelper(self, node, visited, recursionStack):
        visited[node] = True
        recursionStack[node] = True

        print("node = ", node, "visited = ", visited, "recursionStack = ", recursionStack)
        for neighbour in self.graph[node]:
            if visited[neighbour] == False:
                if self.checkCycleHelper(neighbour, visited, recursionStack):
                    return True
            elif recursionStack[neighbour] == True:
                return True

        recursionStack[node] = False
        return False

    def checkCycle(self):
        visited = [False] * self.vertices
        recursionStack = [False] * self.vertices
        
        for node in list(self.graph):
            print("#node = ", node, "visited = ", visited, "recursionStack = ", recursionStack)
            if visited[node] == False:
                if self.checkCycleHelper(node, visited, recursionStack) == True:
                    return True
        
        return False

if __name__ == "__main__":
    import sys

    # python gfg-directed-graph-check-cycle.py 2 [[1,0],[0,1]]
    # python gfg-directed-graph-check-cycle.py 7 [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
    # python gfg-directed-graph-check-cycle.py 4 [[0,1],[1,2],[2,3],[3,0]]
    # python gfg-directed-graph-check-cycle.py 4 [[0,1],[0,2],[1,2],[2,0],[2,3],[3,3]]

    if len(sys.argv) == 3:
        import json
        graph = Graph(int(sys.argv[1]))
        edges = json.loads(sys.argv[2])

        for edge in edges:
            graph.addEdge(int(edge[0]),int(edge[1]))
    else:
        graph = Graph(7)
        graph.addEdge(0,1)
        graph.addEdge(0,2)
        graph.addEdge(1,3)
        graph.addEdge(1,4)
        graph.addEdge(2,5)
        graph.addEdge(2,6)
    
    graph.printGraph()
    if graph.checkCycle():
        print("The graph is cyclic")
    else:
        print("The graph is NOT cyclic")