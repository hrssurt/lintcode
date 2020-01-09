"""***************************  TITLE  ****************************"""
"""1783  Binary Tree Postorder Traversal-null.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree, return the postorder traversal of its nodes' values.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:{1,2,3}
Output:[2,3,1]

Explanation:
  1
 / \
2  3

"""



"""***************************  CODE  ****************************"""
class Solution:
    def postorderTraversal(self, root):
        if not root: return []
        stack, result = [root], []
        while stack:
            root = stack.pop()
            result.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
                
        return result[::-1]
        
            
        
        
