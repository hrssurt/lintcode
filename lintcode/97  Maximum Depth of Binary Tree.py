"""***************************  TITLE  ****************************"""
"""97  Maximum Depth of Binary Tree.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree, find its maximum depth.
"""



"""***************************  EXAMPLES  ****************************"""
"""
5000
"""



"""***************************  CODE  ****************************"""
class Solution:
    def maxDepth(self, root):
        if not root: return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
