from typing import Optional

"""
Question:
You are given the head of a singly linked list head and a positive integer k.

You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on. If there are fewer than k nodes left, leave the nodes as they are.

Return the modified list after reversing the nodes in each group of k.

You are only allowed to modify the nodes' next pointers, not the values of the nodes.

Example 1:

Input: head = [1,2,3,4,5,6], k = 3

Output: [3,2,1,6,5,4]
Example 2:

Input: head = [1,2,3,4,5], k = 3

Output: [3,2,1,4,5]
Constraints:

The length of the linked list is n.
1 <= k <= n <= 100
0 <= Node.val <= 100

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        walker = head
        dummy = ListNode()
        prev = dummy
        def reverse_ll(start):
            prev, cur = None, start
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev, start

        while walker:
            cnt, start = 1, walker
            while walker and cnt<k:
                walker = walker.next
                cnt+=1
            if cnt == k and walker:
                nextNode, walker.next = walker.next, None
                start, end = reverse_ll(start)
                prev.next, prev = start, end
                walker = nextNode
            else:
                prev.next = start
        return dummy.next