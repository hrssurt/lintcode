"""***************************  TITLE  ****************************"""
"""1353  Sum Root to Leaf Numbers.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
"""



"""***************************  EXAMPLES  ****************************"""
"""
0-9
"""



"""***************************  CODE  ****************************"""
class Solution:
    def __init__(self):
        self.sum = 0

    def sumNumbers(self, root):
        def dfs(cur_node, previous_num):
            if not cur_node:
                return
            
            current_num = previous_num * 10 + cur_node.val
            
            if not cur_node.left and not cur_node.right:
                self.sum += current_num
            else:
                dfs(cur_node.left, current_num)
                dfs(cur_node.right, current_num)
            
        dfs(root, 0)
        return self.sum
            
            

