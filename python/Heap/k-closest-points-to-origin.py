# https://leetcode.com/problems/k-closest-points-to-origin/submissions/

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K == len(points):
            return points
        
        heap = []
        heapq.heapify(heap)
        
        # Calculate distances from origin
        for point in points:
            distance = point[0]**2 + point[1]**2
            # https://docs.python.org/3.8/library/heapq.html#basic-examples
            # https://stackoverflow.com/questions/3954530/how-to-make-heapq-evaluate-the-heap-off-of-a-specific-attribute
            # Heap elements can be tuples. Heap will sort by the first element of the tuple
            heapq.heappush(heap, (distance, point))
            
        
        return [ point[1] for point in heapq.nsmallest(K, heap) ]