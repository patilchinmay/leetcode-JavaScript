# https://leetcode.com/problems/binary-tree-right-side-view/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root) -> [int]:
        if not root:
            return []
        
        ans = dict()
        queue = [(root, 0)]
        
        while queue:
            node, level = queue.pop(0)
            
            if node != None:
                
                if level in ans:
                    ans[level].append(node.val)
                else:
                    ans[level] = [node.val]
                    
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
        
        return [ans[level][-1] for level in ans]

# [1,2,3,6,5,7,4]
# [1,2,3,null,5,null,4]
# [1]
# []
# [1,2,3]
# [1,null,2,null,3]
# [1,2]
# [1,2,null,3,null]
# [1,2,null,null,3]