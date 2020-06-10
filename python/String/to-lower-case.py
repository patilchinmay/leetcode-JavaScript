# https://leetcode.com/problems/to-lower-case/submissions/

class Solution:
    def toLowerCase(self, str: str) -> str:
        if not str:
            return ""
        
        answer = []
        
        for char in str:
            if ord('A') <= ord(char) <= ord('Z'):
                answer.append( chr(ord(char) + 32) )
            else:
                answer.append(char)
        
        return ''.join(answer)
        