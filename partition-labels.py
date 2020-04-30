# https://leetcode.com/problems/partition-labels/submissions/

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        characters = set()
        characters.update(list(S))

        # print(characters)

        intervals = []

        for char in characters:
            intervals.append([S.find(char), S.rfind(char)])

        intervals.sort(key=lambda x:x[0])

        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(interval[1], merged[-1][1])

        return [item[1]-item[0]+1 for item in merged]
