# https://leetcode.com/problems/reverse-words-in-a-string/submissions/

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        s.reverse()
        return " ".join(s)