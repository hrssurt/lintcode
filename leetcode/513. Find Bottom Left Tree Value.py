"""***************************  TITLE  ****************************"""
"""513. Find Bottom Left Tree Value.py"""



"""***************************  DESCRIPTION  ****************************"""
"""

Given a binary tree, find the leftmost value in the last row of the tree. 


Example 1:
Input:

    2
   / \
  1   3

Output:
1



  Example 2: 
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7



Note:
You may assume the tree (i.e., the given root node) is not NULL.

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
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = [root]
        
        while q:
            res = q[0].val
            size = len(q)
            for _ in range(size):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        return res
​
