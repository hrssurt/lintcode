"""***************************  TITLE  ****************************"""
"""939  Binary Tree Kth Floor Node.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Return the number of nodes in the kth layer(The layer number starts from 1 and the root node is layer 1).
"""



"""***************************  EXAMPLES  ****************************"""
"""
kth
"""



"""***************************  CODE  ****************************"""
class Solution:
    def kthfloorNode(self, root, k):
        if not root or k == 0:
            return 0
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
            k -= 1
            if k == 0:
                return len(level)
        return 0 # k > height
        
            

