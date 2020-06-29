# https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root) -> [[int]]:
        if root == None:
            return []
        
        ans = {}
        queue = [(root, 0)]
        
        while queue:
            node, level = queue.pop(0)
            
            if node != None:
                
                if level in ans:
                    ans[level].append(node.val)
                else:
                    ans[level]  =  [node.val]
                    
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
        
        # print(ans)
        
        return [ans[level] for level in ans]