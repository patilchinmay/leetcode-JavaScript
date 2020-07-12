# https://leetcode.com/problems/minimum-time-difference/submissions/

class Solution:
    def findMinDifference(self, timePoints: [str]) -> int:
        
        def minuteRepresentation(time):
            return time[0] * 60 + time[1]
        
        MINUTES_IN_DAY = 24*60
        
        min_diff = MINUTES_IN_DAY
        
        times = [ ( int(timePoint.split(':')[0]), int(timePoint.split(':')[1]) ) for timePoint in timePoints]
        
        times.sort(key=lambda x: (x[0], x[1]))
        
        # print(times)
        
        # Check all times
        for i in range(len(times)):
            j = (i + 1) % len(times)
            min_diff = min(min_diff, (minuteRepresentation(times[j]) - minuteRepresentation(times[i])) % MINUTES_IN_DAY)
            # print(i, times[i], minuteRepresentation(times[i]), j, times[j], minuteRepresentation(times[j]), (minuteRepresentation(times[j]) - minuteRepresentation(times[i])) % MINUTES_IN_DAY)
            # print()
        return min_diff
        