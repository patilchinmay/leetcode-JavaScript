# Binary Search

## Template for Binary Search. It takes an array as input and returns the index.

- Time Complexity: O(log⁡N), where NNN is the length of input array A.

- Space Complexity: O(1).

```
def binary_search(self, A: [int]) -> int:
        
        left = 0
        right = len(A)-1
        
        while(left < right):
            middle = left + (right - left) // 2
            
            if A[middle] < A[middle + 1]: # This line should be replaced with required logic
                left = middle + 1
            else:
                right = middle
        
        return left
```
Reference:
- https://leetcode.com/problems/peak-index-in-a-mountain-array/solution/
- https://leetcode.com/explore/learn/card/binary-search/