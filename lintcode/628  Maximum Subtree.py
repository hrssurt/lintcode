"""***************************  TITLE  ****************************"""
"""628  Maximum Subtree.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a binary tree, find the subtree with maximum sum. Return the root of the subtree.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:
{1,-5,2,0,3,-4,-5}
Output:3
Explanation:
The tree is look like this:
     1
   /   \
 -5     2
 / \   /  \
0   3 -4  -5
The sum of subtree 3 (only one node) is the maximum. So we return 3.

"""



"""***************************  CODE  ****************************"""
class Solution:
    def findSubtree(self, root):
        def dfs(root):
            if not root:
                return None, 0, float("-inf")   # max node, sum of tree, max_sum
                
            root_val = root.val
            left_node, left_sum, left_max = dfs(root.left)
            right_node, right_sum, right_max = dfs(root.right)
            sum_of_tree = left_sum + root_val + right_sum
            max_sum = max(sum_of_tree, left_max, right_max)
            if max_sum == left_max:
                return left_node, sum_of_tree, left_max
            elif max_sum == right_max:
                return right_node, sum_of_tree, right_max
            else:  # this root is the new max
                return root, sum_of_tree, max_sum
        return dfs(root)[0]
            
            
