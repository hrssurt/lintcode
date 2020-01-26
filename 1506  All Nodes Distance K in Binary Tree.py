"""***************************  TITLE  ****************************"""
"""1506  All Nodes Distance K in Binary Tree.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
We are given a binary tree (with root node root), a target node, and an integer value K.
"""



"""***************************  EXAMPLES  ****************************"""
"""
root
"""



"""***************************  CODE  ****************************"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the tree
    @param target: the target
    @param K: the given K
    @return: All Nodes Distance K in Binary Tree
    """
    def distanceK(self, root, target, K):
        # Write your code here
        if not root:
            return -1
        
        def connect(root):
            if root.left:
                root.left.parent = root
                connect(root.left)
            
            if root.right:
                root.right.parent = root
                connect(root.right)
                
        connect(root)
        root.parent = None
        
        # now use bfs
        d = 0
        q = [target]
        visited = set()
        visited.add(target)
        while q:
            if d == K:
                return [node.val for node in q]
            size = len(q)
            for _ in range(size):
                node = q.pop(0)
                for neighbour in [node.left, node.right, node.parent]:
                    if neighbour and neighbour not in visited:
                        visited.add(neighbour)
                        q.append(neighbour)
                        
            d += 1
                        
                
        return []
                