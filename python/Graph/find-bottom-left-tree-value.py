# https://leetcode.com/problems/find-bottom-left-tree-value/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root) -> int:
        ans = {}
        maxlevel = -1
        queue = [(root, 0)]
        
        while queue:
            node, level = queue.pop(0)
            
            if node != None:
                if level in ans:
                    ans[level].append(node.val)
                else:
                    ans[level] = [node.val]
                    maxlevel += 1
                
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
        
#         print(ans)
#         print(maxlevel)
        
        return ans[maxlevel][0]