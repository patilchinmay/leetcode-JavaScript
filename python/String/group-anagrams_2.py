# https://leetcode.com/problems/group-anagrams/submissions/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        seen_sorted_lists = []
        
        # The idea is to go through each string and create a sorted list from it and store all the sorted lists. If any sorted list is seen before, that means current string is an anagram of a previously seen string.
        for string in strs:
            list_ = sorted(string)

            if not list_ in seen_sorted_lists:
                result.append([string])
                seen_sorted_lists.append(list_)
            else:
                index = seen_sorted_lists.index(list_)
                result[index].append(string)
                
        return result