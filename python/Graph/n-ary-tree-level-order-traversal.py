# https://leetcode.com/problems/n-ary-tree-level-order-traversal/submissions/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def levelOrder(self, root: 'Node') -> [[int]]:
        
        if root == None:
            return []
        
        ans = {}       
        queue = [(root, 0)]
        
        while queue:
            node, level = queue.pop(0)
            
            if node:
                
                if level in ans:
                    ans[level].append(node.val)
                else:
                    ans[level] = [node.val]
                    
                for child in node.children:
                    queue.append((child, level+1))
        
        # print(ans)
        
        return [ans[level] for level in ans]