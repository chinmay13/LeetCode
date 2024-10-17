from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:   return 0
        res = [0] * len(height)
        i = 0
        j = len(height) - 1
        maxL = height[0]
        maxR = height[-1]

        while (i < j):
            if maxL < maxR:
                i += 1
                res[i] = max(maxL - height[i], 0)
                maxL = max(maxL, height[i])
            else:
                j -= 1
                res[j] = max(maxR - height[j], 0)
                maxR = max(maxR, height[j])
        return sum(res)



