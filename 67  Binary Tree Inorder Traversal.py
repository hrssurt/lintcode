"""***************************  TITLE  ****************************"""
"""67  Binary Tree Inorder Traversal.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree, return the inorder traversal of its nodes' values.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input：{1,2,3}
Output：[2,1,3]
Explanation:
   1
  / \
 2   3
it will be serialized {1,2,3}
Inorder Traversal

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
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        stack, result = [], []
        while root:
            stack.append(root)
            root = root.left
        
        while stack:
            top = stack.pop()
            result.append(top.val)
            if top.right:
                top = top.right
                while top:
                    stack.append(top)
                    top = top.left
        return result
                    
                
            

