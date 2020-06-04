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
    graph = Graph(7)
    graph.addEdge(0,1)
    graph.addEdge(0,2)
    graph.addEdge(1,3)
    graph.addEdge(1,4)
    graph.addEdge(2,5)
    graph.addEdge(2,6)

    # graph = Graph(4)
    # graph.addEdge(0,1)
    # graph.addEdge(1,2)
    # graph.addEdge(2,3)
    # graph.addEdge(3,0)

    graph.printGraph()
    
    graph.bfs(0)