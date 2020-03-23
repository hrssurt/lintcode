"""***************************  TITLE  ****************************"""
"""94. Binary Tree Inorder Traversal.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?

"""



"""***************************  CODE  ****************************"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root: return res
        
        s = []
        cur = root
        while cur:
            s.append(cur)
            cur = cur.left
            
        while s:
            top = s.pop(-1)
            res.append(top.val)
            if top.right:
                top = top.right
                s.append(top)
                
                while top.left:
                    top = top.left
                    s.append(top)
                
        return res
                
                
            
            
        
​
