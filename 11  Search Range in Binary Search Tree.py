"""***************************  TITLE  ****************************"""
"""11  Search Range in Binary Search Tree.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary search tree and a range [k1, k2], return node values within a given range in ascending order.
"""



"""***************************  EXAMPLES  ****************************"""
"""
[k1, k2]
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
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        result = []
        def dfs(root, k1, k2, result):
            if not root: return
            if root.val < k1: # only need to deal with the right subtree
                return dfs(root.right, k1, k2, result)
            if root.val > k2:   # only need to deal with the left subtree
                return dfs(root.left, k1, k2, result)
            else:
                dfs(root.left, k1, k2, result)
                result.append(root.val)
                dfs(root.right, k1,k2, result)
        
        dfs(root, k1, k2, result)  
        return result
