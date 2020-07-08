# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getAllElements(self, root1, root2) -> [int]:
        ans  =  []
        
        self.traverseTree(root1, ans)

        self.traverseTree(root2, ans)

        ans.sort()
        
        return ans
    
    def traverseTree(self, node, ans):
        if node != None:
            
            if node.left != None:
                self.traverseTree(node.left, ans)
            
            ans.append(node.val)
            
            if node.right != None:
                self.traverseTree(node.right, ans)