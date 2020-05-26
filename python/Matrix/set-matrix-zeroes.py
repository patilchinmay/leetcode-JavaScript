# https://leetcode.com/problems/set-matrix-zeroes/submissions/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_with_zero = set()
        cols_with_zero = set()
        
        # Find all rows and cols which contains 0's
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows_with_zero.add(i)
                    cols_with_zero.add(j)
        
        # Make all items in the marked row as 0
        for i in rows_with_zero:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        
        # Make all items in the marked column as 0
        for i in cols_with_zero:
            for j in range(len(matrix)):
                matrix[j][i] = 0