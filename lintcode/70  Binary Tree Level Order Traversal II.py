"""***************************  TITLE  ****************************"""
"""70  Binary Tree Level Order Traversal II.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:
{1,2,3}
Output:
[[2,3],[1]]
Explanation:
    1
   / \
  2   3
it will be serialized {1,2,3}
level order traversal

"""



"""***************************  CODE  ****************************"""
class Solution:
    def levelOrderBottom(self, root):
        q, result = [root], []
        if not root: return result
        while q:
            level, size = [], len(q)
            for _ in range(size):
                node = q.pop(0)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                level.append(node.val)
                
            result.insert(0, level)
        return result

