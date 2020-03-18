"""***************************  TITLE  ****************************"""
"""1197  Find Bottom Left Tree Value.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree, find the leftmost value in the last row of the tree.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:{2,1,3}
Output:1

Explanation:
  2
 /  \
1   3

"""



"""***************************  CODE  ****************************"""
class Solution:
    def findBottomLeftValue(self, root):
        if not root:
            return root
        q = [root]
        while q:
            level = []
            size = len(q)
            for _ in range(size):
                node = q.pop(0)
                level.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return level[0].val

