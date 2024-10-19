from typing import List

"""
Question:
You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

Example 1:

Input: n = 1

Output: ["()"]
Example 2:

Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]
You may return the answer in any order.

Constraints:

1 <= n <= 7

"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stk = [(1, 0,'(')]
        while stk:
            x, y, val = stk.pop()
            if x == y == n:
                res.append(val)
            if x <= n:
                stk.append((x+1, y, val+"("))
            if x>y:
                stk.append((x, y+1, val+")"))
        return res
