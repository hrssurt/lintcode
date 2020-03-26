"""***************************  TITLE  ****************************"""
"""199. Binary Tree Right Side View.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

"""



"""***************************  CODE  ****************************"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        q = [root]
        while q:
            res.append(q[-1].val)
            size = len(q)
            for _ in range(size):
                node = q.pop(0)
​
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
​
        return res
        
            node = q.pop(0)
​
