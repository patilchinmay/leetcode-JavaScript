# Works with directed and undirected graph
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

from collections import defaultdict 

class Graph:
    def __init__(self,vertices):
        self.vertices  = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        # self.graph[v].append(u)   # Uncomment this line for undirected/bidirectional graph
    
    def printGraph(self):
        for node in self.graph:
            print(node, "=" ,self.graph[node])

    def bfs(self, node):
        visited = [False] * self.vertices

        node_queue = []
        node_queue.append(node)
        visited[node] = True

        while node_queue:
            current_node = node_queue.pop(0)
            print(current_node)
            for neighbor in self.graph[current_node]:
                if visited[neighbor] == False:
                    node_queue.append(neighbor)
                    visited[neighbor] = True

if __name__ == "__main__":
    import sys

    # python gfg-graph-bfs.py 2 [[1,0],[0,1]]
    # python gfg-graph-bfs.py 7 [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
    # python gfg-graph-bfs.py 4 [[0,1],[1,2],[2,3],[3,0]]
    # python gfg-graph-bfs.py 4 [[0,1],[0,2],[1,2],[2,0],[2,3],[3,3]]

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
    
    graph.bfs(0)