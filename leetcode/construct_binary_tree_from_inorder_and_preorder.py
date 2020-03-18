# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        
        else:
            root_idx = inorder.index(root.val)
            left_tree_len = root_idx
            root.left = self.buildTree(preorder[1: left_tree_len+1], inorder[:root_idx])
            root.right = self.buildTree(preorder[left_tree_len+1:], inorder[root_idx+1:])
            return root
