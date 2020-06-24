# https://leetcode.com/problems/find-common-characters/submissions/
import collections

class Solution:
    def commonChars(self, A: [str]) -> [str]:
        
        # Handle empty input
        if not A:
            return[]
        
        if len(A) == 1:
            return list(A[0])
        
        counter = collections.Counter(A[0])
        
        for i in range(1, len(A)):
            # https://docs.python.org/3/library/collections.html#collections.Counter
            # c & d (where both are counters)
            # intersection:  min(c[x], d[x])
            counter = counter & collections.Counter(A[i]) 
            
        return counter.elements()