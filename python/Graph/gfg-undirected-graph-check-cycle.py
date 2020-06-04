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
    import sys

    # python gfg-undirected-graph-check-cycle.py 2 [[1,0],[0,1]]
    # python gfg-undirected-graph-check-cycle.py 7 [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
    # python gfg-undirected-graph-check-cycle.py 4 [[0,1],[1,2],[2,3],[3,0]]

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