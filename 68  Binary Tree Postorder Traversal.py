"""***************************  TITLE  ****************************"""
"""68  Binary Tree Postorder Traversal.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree, return the postorder traversal of its nodes' values.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input：{1,2,3}
Output：[2,3,1]
Explanation:  
   1
  / \
 2   3
 it will be serialized {1,2,3}
Post order traversal

"""



"""***************************  CODE  ****************************"""
class Solution:
    def postorderTraversal(self, root):
        cur_node, result, stack = root, [], []
        while cur_node or stack:
            while cur_node:
                stack.append(cur_node)
                if cur_node.left:
                    cur_node = cur_node.left
                elif cur_node.right:
                    cur_node = cur_node.right
                else:
                    break
            
            cur_node = stack.pop(-1)
            result.append(cur_node.val)
            
            # check if cur_node is the left child of previous node
            # that means the left subtree of stack[-1] has been explored
            # so we need to start explore the right subtree of stack[-1]
            if stack and stack[-1].left is cur_node:
                cur_node = stack[-1].right
            else:
                cur_node = None    # so that the previous loop will break
                
        return result
            
            
        
