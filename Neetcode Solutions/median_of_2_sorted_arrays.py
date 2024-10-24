from typing import List
"""
Question:

Median of Two Sorted Arrays
Solved 
You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.

Your solution must run in 
O
(
l
o
g
(
m
+
n
)
)
O(log(m+n)) time.

Example 1:

Input: nums1 = [1,2], nums2 = [3]

Output: 2.0
Explanation: Among [1, 2, 3] the median is 2.

Example 2:

Input: nums1 = [1,3], nums2 = [2,4]

Output: 2.5
Explanation: Among [1, 2, 3, 4] the median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
-10^6 <= nums1[i], nums2[i] <= 10^6

"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        total = len(A)+len(B)
        half = total//2
        if len(nums2)< len(nums1):
            A, B = B, A
        start, end = 0, len(A)-1
        while True:
            i = (start + end)//2
            j = half - i - 2
            leftA = A[i] if i >=0 else float('-inf')
            leftB = B[j] if j >=0 else float('-inf')
            rightA = A[i+1] if (i+1) < len(A) else float('inf')
            rightB = B[j+1] if (j+1) < len(B) else float('inf')

            if leftA <= rightB and leftB <=rightA:
                if total%2==0:
                    return (max(leftA, leftB) + min(rightA, rightB))/2
                else:
                    return min(rightA, rightB)
            elif leftA >= rightB:
                end = i-1
            else:
                start = i+1