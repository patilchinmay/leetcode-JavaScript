# https://leetcode.com/problems/valid-parentheses/submissions/

from collections import deque 

class Solution:
    def isValid(self, s: str) -> bool:
        
        dictionary = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        
        stack = deque()
        
        for char in s:
            if char in dictionary:
                stack.append(char)
            elif stack and stack[-1] in dictionary and char == dictionary[stack[-1]]:
                stack.pop()
            else:
                stack.append(char)

        return True if len(stack) == 0 else False