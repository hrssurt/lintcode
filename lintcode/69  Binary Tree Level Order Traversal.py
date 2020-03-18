"""***************************  TITLE  ****************************"""
"""69  Binary Tree Level Order Traversal.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input：{1,2,3}
Output：[[1],[2,3]]
Explanation：
  1
 / \
2   3
it will be serialized {1,2,3}
level order traversal

"""



"""***************************  CODE  ****************************"""
class Solution:
    def levelOrder(self, root):
        q, result = [], []
        if not root: return []
        q.append(root)
        while q:
            size = len(q)
            level = []
            for _ in range(size):
                node = q.pop(0)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                level.append(node.val)
            result.append(level)
        return result

