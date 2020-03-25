"""***************************  TITLE  ****************************"""
"""662. Maximum Width of Binary Tree.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).


Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).


Example 3:

Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).


Example 4:

Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).




Note: Answer will in the range of 32-bit signed integer.

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
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_width = 1
        
        
        def calculate_width(lst):
            if len(lst) <= 1:
                return len(lst)
            
            left, right = 0 , len(lst) - 1
            while left < right and lst[left][0] is None:
                left += 1
                
            while left < right and lst[right][0] is None:
                right -= 1
                
            if left == right:
                if lst[left][0]:
                    return 1
                else:
                    return 0
                
            else:
                return lst[right][1] - lst[left][1] + 1
                
        
        q = [(root, 0)]
        while q:
            size = len(q)
            max_width = max(max_width, calculate_width(q))
            for _ in range(size):
                n, idx = q.pop(0)
                if n:
                    q.append((n.left, idx * 2))
                    q.append((n.right, idx * 2 + 1))
            
        return max_width
        
​
