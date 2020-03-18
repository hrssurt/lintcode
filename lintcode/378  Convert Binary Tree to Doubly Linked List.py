"""***************************  TITLE  ****************************"""
"""378  Convert Binary Tree to Doubly Linked List.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Convert a binary tree to doubly linked list with in-order traversal.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:
	    4
	   / \
	  2   5
	 / \
	1   3		

Output: 1<->2<->3<->4<->5

"""



"""***************************  CODE  ****************************"""
"""
Definition of Doubly-ListNode
class DoublyListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = nextDefinition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of tree
    @return: the head of doubly list node
    """
    def bstToDoublyList(self, root):
        if not root: return None
        leftLst = self.bstToDoublyList(root.left)
        rightLst = self.bstToDoublyList(root.right)
        cur_node = DoublyListNode(root.val)
        cur_node.next = rightLst
        # now connect leftLst and rightLst to the cur_node
        left_cur = leftLst
        while left_cur and left_cur.next:
            left_cur = left_cur.next
        if left_cur:
            left_cur.next = cur_node
            cur_node.prev = left_cur
        else:
            cur_node.prev = leftLst
        
        if rightLst: rightLst.prev = cur_node
        
        return leftLst if leftLst else cur_node
