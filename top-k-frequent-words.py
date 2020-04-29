# https://leetcode.com/problems/top-k-frequent-words/
# https://leetcode.com/submissions/detail/331880920/

import collections

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)

        counter_sorted = []
        counter_sorted = sorted(counter.items(), key=lambda item: (-item[1], item[0]))

        # print(counter_sorted)

        ans = []

        for i in range(k):
            ans.append(counter_sorted[i][0])

        return ans
