# https://leetcode.com/problems/last-stone-weight/submissions/

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Corner cases        
        if len(stones) == 1:
            return stones[0]
        
        # Python has  min heap by default. Multiplying each item by -1 will create the  effect of max heap by using the underlying min heap
        stones = [i*-1 for i in stones]
        
        # Create heap from input list
        heapq.heapify(stones)
        
        while len(stones) > 1:
            # Size of heap
            # print(len(stones), ":", stones)
            
            # Get two largest from heap
            first = heapq.heappop(stones) * -1
            second = heapq.heappop(stones) * -1
            
            if first != second:
                heapq.heappush(stones, -1*abs(first-second))
                
        # print("FINAL:", len(stones), ":", stones)
        
        if len(stones):
            return -1 * stones[0]
        else:
            return 0