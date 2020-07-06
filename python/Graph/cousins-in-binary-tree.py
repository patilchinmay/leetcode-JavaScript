# https://leetcode.com/problems/cousins-in-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root, x: int, y: int) -> bool:
        queue = [(root, 0, None)]
        
        x_level = 0
        x_parent = None
        x_found = False
        
        y_level = 0
        y_parent = None
        y_found = False
        
        while queue and not (x_found and y_found):
            node, level, parent = queue.pop(0)
            
            if node != None:
                
                if node.val == x:
                    x_level = level
                    x_parent = parent
                    x_found = True
                    
                if node.val == y:
                    y_level = level
                    y_parent = parent
                    y_found = True
                    
                queue.append((node.left, level+1, node))
                queue.append((node.right, level+1, node))
        
        return (x_level == y_level and x_parent != y_parent)