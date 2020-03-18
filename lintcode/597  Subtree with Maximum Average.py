"""***************************  TITLE  ****************************"""
"""597  Subtree with Maximum Average.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input：
{1,-5,11,1,2,4,-2}
Output：11
Explanation:
The tree is look like this:
     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2 
The average of subtree of 11 is 4.3333, is the maximun.

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
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def __init__(self):
        self.cur_max = float("-inf")
        self.cur_node = None
    
    def findSubtree2(self, root):
        self.sum_and_count(root)
        return self.cur_node
        
    def sum_and_count(self, root):
        if not root:
            return 0, 0
        
        left_sum, left_count = self.sum_and_count(root.left)
        right_sum, right_count = self.sum_and_count(root.right)
        
        cur_sum, cur_count = left_sum + root.val + right_sum, left_count + 1 + right_count
        
        if not self.cur_node or cur_sum / cur_count > self.cur_max:
            self.cur_node = root
            self.cur_max = cur_sum / cur_count
            
        return cur_sum, cur_count

