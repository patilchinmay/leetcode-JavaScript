# https://leetcode.com/problems/find-k-closest-elements/submissions/

from collections import deque

class Solution:
    def findClosestElements(self, arr: [int], k: int, x: int) -> [int]:
        if x < arr[0]:
            return arr[:k]
        elif x > arr[-1]:
            return arr[-k:]
        else:
            # index of given number if it exists in the arr or closest index if it doesn't exist in the arr
            # x_index = bisect.bisect(arr, x)
            x_index = self.binarySearchArray(x, arr)
            
            # print("index => ",x_index, ":" ,arr[x_index])

            result = deque()
            
            left = x_index - 1
            right = x_index
            
            while len(result) != k:
                l = arr[left] if left >= 0 else float("inf")
                r = arr[right] if right < len(arr) else float("inf")
                
                if abs(x - l) <= abs(x - r):
                    result.appendleft(l)
                    left -= 1
                else:
                    result.append(r)
                    right += 1
            
            return result
            
    def binarySearchArray(self, number, arr):
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            middle = left + (right-left) // 2
            
            if arr[middle] < number:
                left = middle + 1
            elif arr[middle] > number:
                right = middle - 1
            elif arr[middle] == number:
                return middle
        
        # print(arr[left], number, arr[right])
        
        # Number is not in the arr
        # Find which arr[index] is closest to the number
        if abs(arr[left] - number) < abs(arr[right] - number):
            return left
        else:
            return right

# [1,2,3,4,5]
# 1
# 1
# [1,2,3,4,5]
# 1
# -1
# [1,2,3,4,5]
# 1
# 100
# [1,2,3,4,5]
# 1
# 4
# [1,2,3,4,5]
# 4
# 1
# [1,2,3,4,5]
# 4
# 5
# [1,2,3,4,5]
# 4
# -1
# [1,2,3,4,5]
# 4
# 100
# [1,2,3,4,5]
# 5
# 1
# [1,2,3,4,5]
# 5
# 5
# [1,2,3,4,5]
# 5
# 4
# [1,2,3,4,5]
# 5
# -1
# [1,2,3,4,5]
# 5
# 100
# [1,2,3,4]
# 4
# 1
# [1,2,3,4]
# 4
# 3
# [0,1,1,1,2,3,6,7,8,9]
# 9
# 4
# [0,1,1,1,2,3,6,7,8,9]
# 9
# 5
# [0,0,0,1,3,5,6,7,8,8]
# 2
# 2