# https://leetcode.com/problems/count-complete-tree-nodes/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def countNodes(self, root) -> int:
        
        if not root:
            return 0
        
        count = 0
        
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            count += 1
            
            if node.left != None:
                queue.append(node.left)
            
            if node.right != None:
                queue.append(node.right)
        
        return count