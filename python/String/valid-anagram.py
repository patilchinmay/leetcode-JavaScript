# https://leetcode.com/problems/valid-anagram/submissions/

import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Empty Strings
        if not s and not t:
            return True
        elif not s or not t:
            return False
        
        # Measure characters and their count
        s_counter = collections.Counter(s)
        t_counter = collections.Counter(t)
        
        return s_counter == t_counter