"""***************************  TITLE  ****************************"""
"""1240  Path Sum III.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
You are given a binary tree in which each node contains an integer value.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input：root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
Output：3
Explanation：
      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

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
    """
    @param root: 
    @param sum: 
    @return: the num of sum path
    """
    def pathSum(self, root, sum):
        if not root:
            return 0
        
        return self.pathSum(root.left, sum) + self.pathSum(root.right, sum) + self.helper(root, sum)
        
    def helper(self, root, sum):   # the path has to use root
        if not root:
            return 0
            
        res = 0
        if root.val == sum:
            res += 1
            
        res += self.helper(root.left, sum - root.val) + self.helper(root.right, sum-root.val)
        return res
