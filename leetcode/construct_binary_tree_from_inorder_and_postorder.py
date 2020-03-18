# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, postorder, inorder):
        if not postorder or not inorder:
            return None
        
        root = TreeNode(postorder[-1])
        if len(postorder) == 1:
            return root
        
        else:
            root_idx = inorder.index(root.val)
            left_tree_len = root_idx
            root.left = self.buildTree(postorder[0: left_tree_len], inorder[:root_idx])
            root.right = self.buildTree(postorder[left_tree_len:-1], inorder[root_idx+1:])

            return root

def inorder_traversal(root):
    if not root:
        return []
    stack, res = [], []
    while root:
        stack.append(root)
        root = root.left

    while stack:
        head = stack.pop(-1)
        res.append(head.val)
        if head.right:
            head = head.right
            while head:
                stack.append(head)
                head = head.left
    return res



def preorder_traversal(root):
    if not root:
        return []

    stack, res = [root], []
    while stack:
        top = stack.pop(-1)
        res.append(top.val)
        if top.right:
            stack.append(top.right)
        if top.left:
            stack.append(top.left)
    return res


def postorder_traversal(root):
    if not root:
        return []
    stack, res = [root], []
    while stack:
        top = stack.pop(-1)
        res.append(top.val)
        if top.left:
            stack.append(top.left)
        if top.right:
            stack.append(top.right)

    return res[::-1]


def compareTwoTree(t1, t2):
    if t1 is None and t2 is None:
        return True

    if not t1 or not t2:
        return False

    return t1.val == t2.val and compareTwoTree(t1.left, t2.left) and compareTwoTree(t1.right, t2.right)



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    soln = Solution()
    postorder, inorder = postorder_traversal(root), inorder_traversal(root)
    new_tree = soln.buildTree(postorder, inorder)
    print(compareTwoTree(root, new_tree))

