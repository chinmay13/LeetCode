from typing import Optional, List
"""
Question:
You are given an array of k linked lists lists, where each list is sorted in ascending order.

Return the sorted linked list that is the result of merging all of the individual linked lists.

Example 1:

Input: lists = [[1,2,4],[1,3,5],[3,6]]

Output: [1,1,2,3,3,4,5,6]
Example 2:

Input: lists = []

Output: []
Example 3:

Input: lists = [[]]

Output: []
Constraints:

0 <= lists.length <= 1000
0 <= lists[i].length <= 100
-1000 <= lists[i][j] <= 1000

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[
        ListNode]:
        def merge(l1, l2):
            head = walker = ListNode()
            while l1 and l2:
                if l1.val <= l2.val:
                    walker.next = l1
                    l1 = l1.next
                else:
                    walker.next = l2
                    l2 = l2.next
                walker = walker.next
            walker.next = l1 or l2
            return head.next

        if not lists:
            return None
        # res = lists[0]
        # for i in range (1, len(lists)):
        #     res = merge(res, lists[i])
        # return res
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(merge(l1, l2))
            lists = mergedLists
        return lists[0]



