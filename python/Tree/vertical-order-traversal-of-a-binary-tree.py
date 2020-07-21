# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root) -> [[int]]:
        
        nodes = dict()
        
        def traverse(node, x, y):
            
            if x in nodes:
                nodes[x].append((node.val, y))
            else:
                nodes[x] = [(node.val, y)]
            
            if node.left != None:
                traverse(node.left, x-1, y-1)
            
            if node.right != None:
                traverse(node.right, x+1, y-1)
        
        traverse(root, 0, 0)
        
        for key in nodes:
            nodes[key].sort(key=lambda x: (x[1], -1*x[0]), reverse=True)
            for i in range(len(nodes[key])):
                nodes[key][i] = nodes[key][i][0]
        
        # print(nodes)
        
        return [nodes[x] for x in sorted(nodes.keys())]
        