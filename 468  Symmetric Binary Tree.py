"""***************************  TITLE  ****************************"""
"""468  Symmetric Binary Tree.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: {1,2,2,3,4,4,3}
Output: true
Explanation:
         1
        / \
       2   2
      / \ / \
      3 4 4 3

is a symmetric binary tree.

"""



"""***************************  CODE  ****************************"""
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        
        return self.helper(root.left, root.right)
            
    def helper(self, t1, t2):
        if not t1 and not t2:
            return True
            
        if not t1 or not t2:
            return False
            
        return t1.val == t2.val and self.helper(t1.left, t2.right) and \
                                    self.helper(t1.right, t2.left)

