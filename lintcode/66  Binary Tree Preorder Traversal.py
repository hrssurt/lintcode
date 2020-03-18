"""***************************  TITLE  ****************************"""
"""66  Binary Tree Preorder Traversal.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree, return the preorder traversal of its nodes' values.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input：{1,2,3}
Output：[1,2,3]
Explanation:
   1
  / \
 2   3
it will be serialized {1,2,3}
Preorder traversal

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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        if not root: return []
        stack, result = [root], []
        while stack:
            top = stack.pop()
            result.append(top.val)
            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)
        return result
            

