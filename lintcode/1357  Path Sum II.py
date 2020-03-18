"""***************************  TITLE  ****************************"""
"""1357  Path Sum II.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: root = {5,4,8,11,#,13,4,7,2,#,#,5,1}, sum = 22
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
Output: [[5,4,11,2],[5,8,4,5]]
Explanation:
The sum of the two paths is 22：
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

"""



"""***************************  CODE  ****************************"""
from copy import deepcopy
class Solution:
    """
    @param root: a binary tree
    @param sum: the sum
    @return: the scheme
    """
    def pathSum(self, root, s):
        self.result = []
        if not root:
            return self.result
        
        self.dfs(root, [], s)
        return self.result
        
    def is_leaf(self, node):
        return node and not node.left and not node.right

    def dfs(self, root, path, s):
        if not root:
            return
        
        path.append(root.val)
        if self.is_leaf(root) and root.val == s:
            self.result.append(deepcopy(path))
    
        self.dfs(root.left, path, s - root.val)
        self.dfs(root.right, path, s - root.val)
        path.pop(-1)
        
        
                
