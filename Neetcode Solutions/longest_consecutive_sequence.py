from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for num in nums_set:
            if (num-1) not in nums_set:
                size = 1
                while (num+size) in nums_set:
                    size += 1
                res = max(size, res)
        return res