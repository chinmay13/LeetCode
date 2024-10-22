"""

Question:
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in

O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3
Example 2:

Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1
Constraints:

1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000

"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin_search(start, end):
            if start>end:
                return -1
            mid = (start + end) // 2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                return bin_search(start, mid-1)
            else:
                return bin_search(mid+1, end)
        return bin_search(0, len(nums)-1)
