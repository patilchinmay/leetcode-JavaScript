# https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        heap = []
        heapq.heapify(heap)
        
        self.traverseTreeCreateHeap(root, heap, k)
        
        return heapq.heappop(heap) * -1
        
    def traverseTreeCreateHeap(self, node, heap, k):
        if node.left:
            self.traverseTreeCreateHeap(node.left, heap, k)
            
        if node.val != None: # Need 'None' here as it would otherwise skip the node with val = 0.
            heapq.heappush(heap, -1 * node.val)
            
            if len(heap) > k:
                heapq.heappop(heap)
            
        if node.right:
            self.traverseTreeCreateHeap(node.right, heap, k)