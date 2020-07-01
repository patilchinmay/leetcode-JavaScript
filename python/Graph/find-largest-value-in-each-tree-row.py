# https://leetcode.com/problems/find-largest-value-in-each-tree-row/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root) -> [int]:
        if root is None:
            return []
        
        ans = dict()
        queue = [(root, 0)]
        
        while queue:
            node, level = queue.pop(0)
            
            if node is not None:
                
                if level in ans:
                    ans[level].append(node.val)
                else:
                    ans[level] = [node.val]
                    
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
                
        return [max(ans[level]) for level in ans]