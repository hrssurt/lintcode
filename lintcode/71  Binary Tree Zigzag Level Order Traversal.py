"""***************************  TITLE  ****************************"""
"""71  Binary Tree Zigzag Level Order Traversal.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:{1,2,3}
Output:[[1],[3,2]]
Explanation:
    1
   / \
  2   3
it will be serialized {1,2,3}

"""



"""***************************  CODE  ****************************"""
class Solution:
    def zigzagLevelOrder(self, root):
        q, result, level_count = [root], [], 0
        if not root: return result
        while q:
            size = len(q)
            level = []
            for _ in range(size):
                node = q.pop(0)
                if level_count % 2 == 0:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            result.append(level)
            level_count += 1
        return result

