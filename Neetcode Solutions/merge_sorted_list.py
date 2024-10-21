"""
Question:
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Example 1:



Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]
Example 2:

Input: list1 = [], list2 = [1,2]

Output: [1,2]
Example 3:

Input: list1 = [], list2 = []

Output: []
Constraints:

0 <= The length of the each list <= 100.
-100 <= Node.val <= 100

"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        # if not list1:
        #     return list2
        # if not list2:
        #     return list1
        # l1_prev, l2_prev = None, None
        # l1_walk = list1
        # l2_walk = list2

        # while l1_walk and l2_walk:
        #     if l1_walk.val<l2_walk.val:
        #         l1_prev = l1_walk
        #         l1_walk = l1_walk.next
        #         if not l1_walk or l1_walk.val>=l2_walk.val:
        #             l1_prev.next = l2_walk
        #     else:
        #         l2_prev = l2_walk
        #         l2_walk = l2_walk.next
        #         if not l2_walk or l1_walk.val<l2_walk.val:
        #             l2_prev.next = l1_walk

        # return list1 if list1.val<list2.val else list2

        head = walker = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                walker.next = list1
                list1 = list1.next
            else:
                walker.next = list2
                list2 = list2.next
            walker = walker.next
        walker.next = list1 or list2

        return head.next
