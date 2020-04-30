# https://leetcode.com/problems/search-suggestions-system/
# https://leetcode.com/submissions/detail/332195475/
import re

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        products.sort()

        for i in range(len(searchWord)):
            currentTerm = searchWord[:i+1]

            r = re.compile(currentTerm+'.*$')

            suggestions = list(filter(r.match, products))

            # print(currentTerm, suggestions)

            if len(suggestions) < 3:
                ans.append(suggestions)
            else:
                ans.append(suggestions[:3])

        return ans
