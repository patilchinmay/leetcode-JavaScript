# https://leetcode.com/problems/convert-a-number-to-hexadecimal/submissions/

class Solution:
	def toHex(self, num: int) -> str:
		table = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
		result = ''
		
		if num < 0:
			num = 4294967296 + num
			
		while num:
			remainder = num % 16
			num = num // 16
			result = table[remainder] + result

		return result or "0"