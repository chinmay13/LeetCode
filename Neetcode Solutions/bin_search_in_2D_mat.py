"""
Question:
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:



Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

Output: true
Example 2:



Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

Output: false
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bin_search(start, end, row):
            if start>end:
                return False
            mid = (start + end)//2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                return bin_search(start, mid-1, row)
            else:
                return bin_search(mid+1, end, row)
        top = 0
        end = len(matrix)-1
        print(top, end)
        while top<=end:
            mid = (top + end) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return bin_search(0, len(matrix[mid])-1, matrix[mid])
            if matrix[mid][-1]<target:
                top = mid+1
            else:
                end = mid-1
        return False
