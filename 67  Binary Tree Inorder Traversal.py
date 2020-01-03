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
        cur, stack, result = root, [], []
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop(-1)
                result.append(cur.val)
                cur = cur.right
        return result
                    
                
            

