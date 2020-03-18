"""***************************  TITLE  ****************************"""
"""469  Same Tree.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Check if two binary trees are identical. Identical means the two binary trees have the same structure and every identical position has the same value.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:{1,2,2,4},{1,2,2,4}
Output:true
Explanation:
        1                   1
       / \                 / \
      2   2   and         2   2
     /                   /
    4                   4

are identical.

"""



"""***************************  CODE  ****************************"""
class Solution:
    def isIdentical(self, a, b):
        if not a and not b:
            return True
        if (a and not b) or (b and not a):
            return False
        if a.val != b.val:
            return False
        return self.isIdentical(a.left, b.left) and self.isIdentical(a.right, b.right)

