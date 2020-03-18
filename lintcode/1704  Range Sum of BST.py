"""***************************  TITLE  ****************************"""
"""1704  Range Sum of BST.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

"""



"""***************************  CODE  ****************************"""
class Solution:
    def rec(self, root, L, R):
        # write your code her
        if not root or L > R:
            return 0
        
        if root.val < L:
            return self.rec(root.right, L, R)
        
        if root.val > R:
            return self.rec(root.left, L, R)
        
        else:
            s = root.val
            s += self.rec(root.left, L, root.val)
            s += self.rec(root.right, root.val, R)
            return s
            
        
    def rangeSumBST(self, root, L, R):
        return self.rec(root, L, R)

            
