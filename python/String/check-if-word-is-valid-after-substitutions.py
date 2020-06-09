# https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/submissions/

class Solution:
    def isValid(self, S: str) -> bool:
        
        S = S.split("abc")
        S = ''.join(S)
        
        if len(S)>2:
            while True:
                if 'abc' in S:
                    S = S.replace('abc', '')
                else:
                    break
        
        return True if S == '' else False
    
# "aaabcbcbc"
# "a"
# "b"
# "c"
# "ab"
# "bc"
# "ac"
# "abc"
# "abcabc"
# "aabcbc"
# "abcabcababcc"
# "abccba"
# "cababc"