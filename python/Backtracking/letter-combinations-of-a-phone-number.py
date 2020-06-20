# https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/

class Solution:
    dig_dict = {
            '2': ['a','b','c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
    
    def letterCombinations(self, digits: str) -> [str]:   
        if digits == "":
            return []
        
        answer = []
        path = []
        
        self.backtrack(0, digits, path, answer)
        
        return answer
    
    def backtrack(self, index, digits, path, answer):
        # Conditions and Boundaries
        if index == len(digits):
            answer.append("".join(path.copy()))
            return
        
        # Process the node.
        # No processing required
        
        # Call the neighbours i.e. items from dig_dict[digit]
        for i in range(len(self.dig_dict[digits[index]])):
            
            path.append( self.dig_dict[digits[index]][i] )
            
            self.backtrack(index+1, digits, path, answer)
            
            path.pop() # Backtrack
            