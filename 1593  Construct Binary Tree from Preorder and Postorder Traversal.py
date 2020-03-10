"""***************************  TITLE  ****************************"""
"""1593  Construct Binary Tree from Preorder and Postorder Traversal.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
考点：
"""



"""***************************  EXAMPLES  ****************************"""
"""
# This reference program is provided by @jiuzhang.com
# Copyright is reserved. Please indicate the source for forwarding

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution(object):
    def constructFromPrePost(self, pre, post):
        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) == 1: return root

        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:L+1], post[:L])
        root.right = self.constructFromPrePost(pre[L+1:], post[L:-1])
        return root
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
    def constructFromPrePost(self, pre, post):
        if not pre or not post:
            return None
            
        if len(pre) == 1:
            return TreeNode(pre[0])
        
        else:
            root = TreeNode(pre[0])
            left_head = pre[1]
            left_head_idx = post.index(left_head)
            left_subtree_len = left_head_idx + 1
            root.left = self.constructFromPrePost(pre[1:left_subtree_len+1], post[:left_head_idx+1],)
            root.right = self.constructFromPrePost(pre[left_subtree_len+1:], post[left_head_idx+1:-1])
            
            return root
