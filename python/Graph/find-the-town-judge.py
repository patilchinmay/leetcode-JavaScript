# https://leetcode.com/problems/find-the-town-judge/submissions/

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            if N == 1:
                return 1
            else:
                return -1
        
        trustlist = [ [] for i in range(N) ]
        
        # List of [ Node's Trusted Nodes], [0] => 1st item's trusted nodes. [1] => 2nd items trusted nodes.
        for i in range(len(trust)):
            trustlist[trust[i][0]-1].append(trust[i][1])
        
        # print(trustlist)
        judge = -1
        
        # There is one node that doesn't trust anyone
        if trustlist.count([]) == 1:
            judge = trustlist.index([]) + 1
        else:
            return -1
        
        # Remove the judge's node so that we can take intersection of all other nodes and check if the common item is judge
        trustlist.remove([])
        
        # No common trusted element in all nodes/persons
        if not set.intersection(*map(set,trustlist)):
            return -1
        
        # Common trusted in all nodes is judge
        if judge in set.intersection(*map(set,trustlist)):
            return judge
        else:
            return -1

# 2
# []
# 1
# []
# 2
# [[1,2]]
# 3
# [[1,3],[2,3]]
# 3
# [[1,3],[2,3],[3,1]]
# 3
# [[1,2],[2,3]]
# 4
# [[1,3],[1,4],[2,3],[2,4],[4,3]]