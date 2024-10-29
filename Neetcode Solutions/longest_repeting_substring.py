"""

Question:
Longest Repeating Substring With Replacement
Solved
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5
Constraints:

1 <= s.length <= 1000
0 <= k <= s.length


"""
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0
        char_dict = defaultdict(int)
        res = max_val = 0
        while j<len(s):
            char_dict[s[j]] += 1
            max_val = max(max_val, char_dict[s[j]])
            if (k>=(j-i+1-max_val)):
                res = max(res, j-i+1)
            else:
                char_dict[s[i]] -= 1
                i += 1
            j += 1
        return res