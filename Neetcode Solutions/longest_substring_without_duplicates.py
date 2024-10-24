"""
Question:
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"

Output: 1
Constraints:

0 <= s.length <= 1000
s may consist of printable ASCII characters.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        size = 0
        chars = set()
        j = 0
        for i in range(len(s)):
            if s[i] not in chars:
                chars.add(s[i])
                size += 1
                res = max(res, size)
            else:
                while s[j] != s[i]:
                    chars.remove(s[j])
                    size -= 1
                    j += 1
                j += 1
        return res



