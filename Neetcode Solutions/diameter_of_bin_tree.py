"""

Question:

The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.

The length of a path between two nodes in a binary tree is the number of edges between the nodes.

Given the root of a binary tree root, return the diameter of the tree.

Example 1:



Input: root = [1,null,2,3,4,5]

Output: 3
Explanation: 3 is the length of the path [1,2,3,5] or [5,3,2,4].

Example 2:

Input: root = [1,2,3]

Output: 2
Constraints:

1 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100

"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # def max_height(root):
        #     if not root:
        #         return 0
        #     else:
        #         return 1+ max(max_height(root.left), max_height(root.right))

        # def helper(root):
        #     return (max_height(root.left)) + (max_height(root.right))

        # def traverse(root):
        #     maxVal = 0
        #     q = deque()
        #     q.append(root)
        #     while q:
        #         root = q.popleft()
        #         maxVal = max(maxVal, helper(root))
        #         if root.left:
        #             q.append(root.left)
        #         if root.right:
        #             q.append(root.right)
        #     return maxVal

        # return traverse(root)

        res = 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            nonlocal res
            res = max(res, left + right)
            return max(left, right) + 1

        dfs(root)
        return res
