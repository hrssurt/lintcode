"""***************************  TITLE  ****************************"""
"""1181  Diameter of Binary Tree.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

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
    @param root: a root of binary tree
    @return: return a integer
    """
    def __init__(self):
        self.max = 0
    
    def diameterOfBinaryTree(self, root):
        
        if not root:
            return 0
        
        def height(root):
            if not root:
                return 0
            
            lh, rh = height(root.left), height(root.right)
            self.max = max(lh+rh, self.max)
            return max(lh, rh) + 1
        
        
        height(root)
        return self.max
