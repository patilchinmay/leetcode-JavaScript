# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def verticalTraversal(self, root) -> [[int]]:
        
        nodes = defaultdict(list)
        
        def traverse(node, x, y):
            
            nodes[x].append((node.val, y))

            if node.left != None:
                traverse(node.left, x-1, y-1)
            
            if node.right != None:
                traverse(node.right, x+1, y-1)
        
        traverse(root, 0, 0)
        
        for key in nodes:
            # Sort the items in a level as per given constrains
            nodes[key].sort(key=lambda x: (x[1], -1*x[0]), reverse=True)
            # Remove y's from the list
            nodes[key] = [item[0] for item in nodes[key]]
        
        # print(nodes)
        
        return [nodes[x] for x in sorted(nodes.keys())]
        