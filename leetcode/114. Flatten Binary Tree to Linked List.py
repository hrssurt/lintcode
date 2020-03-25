"""***************************  TITLE  ****************************"""
"""114. Flatten Binary Tree to Linked List.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6


The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6


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
    def flatten(self, root: TreeNode) -> None:
        if not root: return None
        l = self.flatten(root.left)
        r = self.flatten(root.right)
        
        root.left = None
        
        if not l:
            root.right = r
        else:                   # l is not empty
            cur = l
            while cur.right:    # traverse till the end
                cur = cur.right
            cur.right = r
            root.right = l
        return root
​
        
            
        
        
        
    
        
        root.left = None
​
