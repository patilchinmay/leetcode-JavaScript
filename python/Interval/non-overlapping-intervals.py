# https://leetcode.com/problems/non-overlapping-intervals/submissions/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sorting to get proper order w.r.t first item
        intervals.sort(key=lambda x:x[0])
        
        count = 0
        i = len(intervals)-1
        
        if i == 0: return 0
        
        # print("Before = ",intervals)
        
        while i > 0:
            # print(i , intervals[i])

            # Duplicates
            if intervals[i] == intervals[i-1]:
                count+=1
                del intervals[i]

            # Check if previous element is not in proper order
            elif not intervals[i][0] >= intervals[i-1][1]:
                count+=1
                del intervals[i-1]
            
            i-=1
            
        # print("After = ",intervals)
        
        return count