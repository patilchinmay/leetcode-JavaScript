# https://leetcode.com/problems/first-missing-positive/submissions/

class Solution:
	def firstMissingPositive(self, nums: List[int]) -> int:
		if not nums:
			return 1
		
		nums = list(set(nums))
		nums.sort()
		
		# Remove all elements smaller than 0
		nums = [item for item in nums if item > 0]

		# Return 1 if list is empty because all elements were smaller than 0
		if not nums:
			return 1
		
		if nums[0] == 1:
			if nums[-1] == len(nums): # All contiguous elements starting from 1 to len(nums), ans will be last item+1
				return nums[-1]+1
			else: # There is some gap in list that start with 1 and doesn't end with len(nums)
				for i, v in enumerate(nums):
					# print(i, v)
					if i != v-1:
						return i+1
		else:
			return 1    # Any list that has positive integers and doesn't start with 1, the answer will be 1

# [0,0,0,0]
# [-1,-2,-3,-4]
# [1,2,0]
# [3,4,-1,1]
# [3,2,4,-1,1]
# [7,8,9,11,12]
# [2,3,4,6,-1,1]