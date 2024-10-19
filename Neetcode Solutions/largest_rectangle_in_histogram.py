"""
Question:
You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Note: This chart is known as a histogram.

Example 1:

Input: heights = [7,1,7,2,2,4]

Output: 8
Example 2:

Input: heights = [1,3,7]

Output: 7
Constraints:

1 <= heights.length <= 1000.
0 <= heights[i] <= 1000

"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        maxHeight = 0
        for i, h in enumerate(heights):
            ti = i
            while stk and stk[-1][1] > h:
                ti, th = stk.pop()
                maxHeight = max(maxHeight, (i - ti)*th )
            stk.append((ti, h))

        while stk:
            maxHeight = max(maxHeight, (len(heights)-stk[-1][0])*stk[-1][1])
            stk.pop()
        return maxHeight