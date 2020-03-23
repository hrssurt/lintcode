"""***************************  TITLE  ****************************"""
"""617. Merge Two Binary Trees.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7


 

Note: The merging process must start from the root nodes of both trees.

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
    
    # return the 
    def copyTree(self, node):
        if not node: 
            return None
        else:
            new = TreeNode(node.val)
            new.left = self.copyTree(node.left)
            new.right = self.copyTree(node.right)
            return new
    
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1: return self.copyTree(t2)
        if not t2: return self.copyTree(t1)
        
        head = TreeNode(t1.val + t2.val)
        head.left = self.mergeTrees(t1.left, t2.left)
        head.right = self.mergeTrees(t1.right, t2.right)
        
        return head
        
​
