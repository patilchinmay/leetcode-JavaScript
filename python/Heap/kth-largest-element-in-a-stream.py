# https://leetcode.com/problems/kth-largest-element-in-a-stream/submissions/

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.target = []
        
        for value in nums:
            self.add(value)

    def add(self, val: int) -> int:
        heappush(self.target, val)
        
        if len(self.target) > self.k:
            
            heappop(self.target)
        
        # print(val, self.target)
        
        return self.target[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)