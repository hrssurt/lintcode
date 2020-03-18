"""***************************  TITLE  ****************************"""
"""1033  Minimum Difference Between BST Nodes.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: root = {4,2,6,1,3,#,#}
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree {4,2,6,1,3,#,#} is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.

"""



"""***************************  CODE  ****************************"""
class Solution:
    def __init__(self):
        self.result = []
    
    def minDiffInBST(self, root):
        self.dfs(root)
        min_diff = float("inf")
        for idx in range(1, len(self.result)):
            min_diff = min(min_diff, self.result[idx] - self.result[idx-1])
        return min_diff
        
    def dfs(self, root):
        if root:
            self.dfs(root.left)
            self.result.append(root.val)
            self.dfs(root.right)
        
        

