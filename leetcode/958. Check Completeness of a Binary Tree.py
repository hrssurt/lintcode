"""***************************  TITLE  ****************************"""
"""958. Check Completeness of a Binary Tree.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

Example 1:



Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.



Example 2:



Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.


 


Note:


	The tree will have between 1 and 100 nodes.


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
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root: return True
        
        q = [root]
        saw_null_pointer = False
​
        while q:
            size = len(q)
            for _ in range(size):
                n = q.pop(0)
                if n is not None: 
                    if saw_null_pointer:
                        return False
                    else:
                        q.append(n.left)
                        q.append(n.right)
                else:   # n is None
                    saw_null_pointer = True
            
        return True
        
        
​
