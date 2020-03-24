"""***************************  TITLE  ****************************"""
"""515. Find Largest Value in Each Tree Row.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]



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
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        q = [root]
        res = []
        while q:
            size = len(q)
            max_n = max([node.val for node in q])
            res.append(max_n)
            for _ in range(size):
                top = q.pop(0)
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
                    
        return res
                
        
​
