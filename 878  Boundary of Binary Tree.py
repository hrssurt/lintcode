"""***************************  TITLE  ****************************"""
"""878  Boundary of Binary Tree.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: {1,#,2,3,4}
Output: [1,3,4,2]
Explanation: 
  1
   \
    2
   / \
  3   4
  The root doesn't have left subtree, so the root itself is left boundary.
  The leaves are node 3 and 4.
  The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
  So order them in anti-clockwise without duplicates and we have [1,3,4,2].

"""



"""***************************  CODE  ****************************"""
class Solution:
    def boundaryOfBinaryTree(self, root):
        if not root:
            return []
    
        def get_left_boundary(root):
            result = []
            while root:
                result.append(root)
                if root.left:
                    root = root.left
                elif root.right:
                    root = root.right
                else:                   # excluding the leafs
                    break
            return result
            
        def get_right_boundary(root):
            result = []
            while root:
                result.append(root)
                if root.right:
                    root = root.right
                elif root.left:
                    root = root.left
                else:               # excluding the leafs
                    break
            return list(reversed(result))
            
        
        def get_leafs(root):
            stack = [root]
