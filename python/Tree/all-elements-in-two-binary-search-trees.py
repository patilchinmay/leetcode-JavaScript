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
    
    def traverseTree(self, root, ans):
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            
            if node != None:
                ans.append(node.val)
                
                if node.left != None:
                    queue.append(node.left)

                if node.right != None:
                    queue.append(node.right)
        
        return