# https://leetcode.com/problems/top-k-frequent-elements/submissions/
# https://leetcode.com/submissions/detail/331417665/

import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        ans = [];
        for number, count in counter.most_common(k):
            ans.append(number)

        return ans
