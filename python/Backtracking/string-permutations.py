# Not a leetcode problem
# Print all permutaions of string
# if given AB, print AB, BA
# if given ABC, print ABC, ACB, BAC, BCA, CAB, CBA
# Order of printing does not matter
# Explanation: https://www.youtube.com/watch?v=GuTPwotSdYw

class Solution:
	answer = []

	def string_permutations(self, string):

		self.backtrack_and_swap(0, list(string))
		print(len(self.answer), "substrings for string", string)
		print(self.answer)
	
	def backtrack_and_swap(self, index, string):
		if index == len(string):
			self.answer.append(string)
			return

		for i in range(index, len(string)):
			string[index], string[i] = string[i], string[index]
			self.backtrack_and_swap(index+1, list(string))
			string[i], string[index] = string[index], string[i]

if __name__ == "__main__":
	solution = Solution()
	solution.string_permutations("123")