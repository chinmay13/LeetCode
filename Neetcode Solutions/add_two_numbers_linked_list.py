from typing import Optional
"""

You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.

Example 1:



Input: l1 = [1,2,3], l2 = [4,5,6]

Output: [5,7,9]

Explanation: 321 + 654 = 975.
Example 2:

Input: l1 = [9], l2 = [9]

Output: [8,1]
Constraints:

1 <= l1.length, l2.length <= 100.
0 <= Node.val <= 9

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> \
    Optional[ListNode]:
        walker1 = l1
        walker2 = l2
        res = res_walker = ListNode()
        carry = 0
        while walker1 or walker2:
            val1 = walker1.val if walker1 else 0
            val2 = walker2.val if walker2 else 0
            temp = val1 + val2 + carry
            carry = 1 if temp > 9 else 0
            res_walker.next = ListNode(temp % 10)
            res_walker = res_walker.next
            walker1 = walker1.next if walker1 else walker1
            walker2 = walker2.next if walker2 else walker2
        if carry:
            res_walker.next = ListNode(carry)
        return res.next


