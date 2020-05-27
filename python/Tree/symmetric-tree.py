# https://leetcode.com/problems/symmetric-tree/
# https://leetcode.com/problems/symmetric-tree/discuss/451092/Python-O(-n-)-by-DFS-and-BFS.-87%2B-w-Visualization

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if root:
            return self.checkSymmetry(root, root)
        else:
            return True
        
    def checkSymmetry(self, p, q):
        if p and q:
            # Check value at both nodes and rucursively call this function for two subtrees.
            return p.val == q.val and self.checkSymmetry(p.left,q.right) and self.checkSymmetry(p.right,q.left)
        elif not p and not q:
            # Both nodes do not exist
            return True
        else:
            # One of the nodes doesn't exist
            return False