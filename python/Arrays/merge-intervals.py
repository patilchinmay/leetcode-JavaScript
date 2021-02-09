# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        
        answer = [intervals[0]]
                
        for i in range(1, len(intervals)):
            if answer[-1][1] >= intervals[i][0]:
                answer[-1][1] = max(intervals[i][1], answer[-1][1])
            else:
                answer.append(intervals[i])
        
        return answer