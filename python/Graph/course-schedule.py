# https://leetcode.com/problems/course-schedule/submissions/
# https://www.geeksforgeeks.org/detect-cycle-in-a-graph/

class Solution:
    
    def checkCycleHelper(self, node, visited, recursionStack):
        visited[node] = True
        recursionStack[node] = True

        for neighbour in self.graph[node]:
            if visited[neighbour] == False:
                if self.checkCycleHelper(neighbour, visited, recursionStack):
                    return True
            elif recursionStack[neighbour] == True:
                return True

        recursionStack[node] = False
        return False
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        from collections import defaultdict 
        self.graph = defaultdict(list)
        
        for edge in prerequisites:
            self.graph[edge[0]].append(edge[1])
        
        visited = [False] * numCourses
        recursionStack = [False] * numCourses
        
        for node in list(self.graph):
            if visited[node] == False:
                if self.checkCycleHelper(node, visited, recursionStack) == True:
                    return False
        
        return True