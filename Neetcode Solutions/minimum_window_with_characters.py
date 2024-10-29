from collections import Counter, defaultdict
"""
Question:
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".
You may assume that the correct output is always unique.

Example 1:
Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:
Input: s = "xyz", t = "xyz"

Output: "xyz"
Example 3:

Input: s = "x", t = "xy"

Output: ""
Constraints:

1 <= s.length <= 1000
1 <= t.length <= 1000
s and t consist of uppercase and lowercase English letters.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = s + t
        t_dict = dict(Counter(t))
        s_dict = defaultdict(int)
        i = j = 0
        chars_matched = set()
        while j < len(s):
            s_dict[s[j]] += 1
            if s[j] in t_dict:
                if t_dict[s[j]] == s_dict[s[j]]:
                    chars_matched.add(s[j])
            while i <= j and (
                    s[i] not in t_dict or s_dict[s[i]] > t_dict[s[i]]):
                s_dict[s[i]] -= 1
                i += 1
            if len(chars_matched) == len(t_dict):
                res = s[i:j + 1] if (j - i + 1) < len(res) else res
            j += 1
        return res if res != s + t else ""

