# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_nums = [str(x) for x in digits]
        
        number = "".join(str_nums)
        
        number = int(number)
        
        number+=1
        
        return list(str(number))