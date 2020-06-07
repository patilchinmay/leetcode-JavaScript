# https://leetcode.com/problems/group-anagrams/submissions/

import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        seen_counters = []
        
        # The idea is to go through each string and create a counter from it and store all the counters. If any counter is seen before, that means current string is an anagram of a previously seen string.
        
        for string in strs:
            counter = collections.Counter(string)

            if not counter in seen_counters:
                result.append([string])
                seen_counters.append(counter)
            else:
                index = seen_counters.index(counter)
                result[index].append(string)
                
        return result