"""***************************  TITLE  ****************************"""
"""68  Binary Tree Postorder Traversal.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree, return the postorder traversal of its nodes' values.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input：{1,2,3}
Output：[2,3,1]
Explanation:  
   1
  / \
 2   3
 it will be serialized {1,2,3}
Post order traversal

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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        if not root:
            return []
        stack, res = [root], []
        while stack:
            top = stack.pop(-1)
            res.append(top.val)
            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)
    
        return res[::-1]


