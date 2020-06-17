# https://leetcode.com/problems/sort-characters-by-frequency/submissions/

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        
        ans = ""
        
        for k, v in counter.most_common():
            ans += v*k
            
        return ans