# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, postorder: List[int], inorder: List[int]) -> TreeNode:
        if not postorder or not inorder:
            return None
        
        root = TreeNode(postorder[0])
        if len(postorder) == 1:
            return root
        
        else:
            root_idx = inorder.index(root.val)
            left_tree_len = root_idx
            root.left = self.buildTree(postorder[0: left_tree_len+1], inorder[:root_idx])
            root.right = self.buildTree(postorder[left_tree_len+1:-1], inorder[root_idx+1:])

            return root

def inorder_traversal(root):
    if not root:
        return []
    stack = [root]
    while stack:
        root = stack.pop(-1)
        while root.left:
            stack.append(root)
            root = root.left

        

def postorder_traversal(root):
    pass




if __name__ == '__main__':
