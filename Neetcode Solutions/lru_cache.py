
"""

Question:

Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

LRUCache(int capacity) Initialize the LRU cache of size capacity.
int get(int key) Return the value cooresponding to the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in
O
(
1
)
O(1) average time complexity.

Example 1:

Input:
["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]

Output:
[null, null, 10, null, null, 20, -1]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 10);  // cache: {1=10}
lRUCache.get(1);      // return 10
lRUCache.put(2, 20);  // cache: {1=10, 2=20}
lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
lRUCache.get(2);      // returns 20
lRUCache.get(1);      // return -1 (not found)
Constraints:

1 <= capacity <= 100
0 <= key <= 1000
0 <= value <= 1000
"""
################################################################################
# Utilizing python dictionary maintaining insertion order:
# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.lru = dict()
#         self.capacity = capacity
#
#     def get(self, key: int) -> int:
#         val = -1
#         if key in self.lru:
#             val = self.lru[key]
#             self.lru.pop(key)
#             self.lru[key] = val
#         return val
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.lru:
#             self.lru.pop(key)
#         else:
#             if len(self.lru) >= self.capacity:
#                 for i in self.lru:
#                     self.lru.pop(i)
#                     break
#
#         self.lru[key] = value

#################### LRU CACHE with doubly linked list

from dataclasses import dataclass

@dataclass
class Node:
    val: int
    key: int
    next: None
    prev: None


class LRUCache:
    def __init__(self, capacity: int):
        self.lru = dict()
        self.capacity = capacity
        self.head = Node(-1, -1, None, None)
        self.end = Node(-1, -1, None, self.head)
        self.head.next = self.end

    def get(self, key: int) -> int:
        val = -1
        if key in self.lru:
            node = self.lru[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.end
            node.prev = self.end.prev
            node.prev.next = node
            self.end.prev = node
            val = node.val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            node = self.lru[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            if len(self.lru) == self.capacity:
                node_to_pop = self.lru.pop(self.head.next.key)
                node_to_pop.next.prev = node_to_pop.prev
                node_to_pop.prev.next = node_to_pop.next
            node = Node(value, key, None, None)
            self.lru[key] = node
        node.next = self.end
        node.prev = self.end.prev
        node.prev.next = node
        self.end.prev = node


