# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/submissions/

import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        target = [] # will maintain k item heap
                        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                heapq.heappush(target, matrix[i][j])
                
                if len(target) > k:
                    heappop(target)
                    
        print(heapq.nlargest(len(matrix)**2-k+1, target))
        
        return heapq.nlargest(len(matrix)**2-k+1, target)[-1]