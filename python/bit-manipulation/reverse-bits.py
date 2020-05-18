# https://leetcode.com/problems/reverse-bits/submissions/

class Solution:
    def reverseBits(self, n: int) -> int:
        # Convert number to binary, remove '0b' at the beginning, fill 0s to make it 32 bit
        num = bin(n)[2:].zfill(32)
        
        return int(num[::-1], 2)