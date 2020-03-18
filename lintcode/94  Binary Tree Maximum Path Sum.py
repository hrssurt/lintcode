"""***************************  TITLE  ****************************"""
"""94  Binary Tree Maximum Path Sum.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree, find the maximum path sum.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Example 1:
	Input:  For the following binary tree（only one node）:
	2
	Output：2
	
Example 2:
	Input:  For the following binary tree:

      1
     / \
    2   3
		
	Output: 6

	

"""



"""***************************  CODE  ****************************"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    def maxPathSum(self, root):
        if not root: return 0
        self.cur_max = float("-inf")
        self.maxPathRoot(root)
        return self.cur_max
        
    
    # max sum we can get by must using root and at most one children
    def maxPathRoot(self, root):
        if not root: return float("-inf")
        l = max(0, self.maxPathRoot(root.left))
        r = max(0, self.maxPathRoot(root.right))
        self.cur_max = max(self.cur_max, l + r + root.val)
        return max(root.val + r, root.val + l)
        
