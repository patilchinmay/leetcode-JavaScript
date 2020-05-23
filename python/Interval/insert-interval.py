# https://leetcode.com/problems/insert-interval/submissions/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals = sorted(intervals+[newInterval], key = lambda x:x[0])
        
        output = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], intervals[i][1])
            else:
                output.append(intervals[i])
                
        return output