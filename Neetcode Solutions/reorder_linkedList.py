from typing import Optional

"""
Question:
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Example 1:

Input: head = [2,4,6,8]

Output: [2,8,4,6]
Example 2:

Input: head = [2,4,6,8,10]

Output: [2,10,4,8,6]
Constraints:

1 <= Length of the list <= 1000.
1 <= Node.val <= 1000

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or head.next == None:
            return
        slow = fast = head
        while fast and fast.next:
            if fast.next.next:
                fast = fast.next.next
                slow = slow.next
            else:
                fast = fast.next

        temp = slow.next
        slow.next = slow_prev = None
        slow = temp
        while slow:
            temp = slow.next
            slow.next = slow_prev
            slow_prev = slow
            slow = temp

        walker = head
        slow = head.next
        c = 1
        while slow and fast:
            if c % 2 == 0:
                walker.next = slow
                slow = slow.next
            else:
                walker.next = fast
                fast = fast.next
            walker = walker.next
            c += 1
        walker.next = slow or fast