# https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = set()
        available = [i+1 for i in range(n)]
        chosen = []
        index = 0
        
        # self.backtrack(available, chosen, ans, k, index)
        self.backtrack(available, [], 0, k)
        
        return self.ans
    
#     def backtrack(self, available, chosen, ans, k, index):
        
#         if len(chosen) == k:
#             ans.add(tuple(sorted(chosen)))
#             return
        
#         for i in range(len(available)):
#             chosen.append(available.pop(i))
            
#             self.backtrack(available, chosen, ans, k, index+1)
            
#             available.insert(i, chosen.pop())   


    def backtrack(self, nums, path, index, k):
        if len(path) == k:
            self.ans.add(tuple(sorted(path)))
            return
        
        if index == len(nums):
            return 
        
        path.append(nums[index])
        
        self.backtrack(nums, path, index+1, k)
        
        path.pop()
        
        self.backtrack(nums, path, index+1, k)
        