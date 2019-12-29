/****************************  TITLE  *****************************/
/*106  Convert Sorted List to Binary Search Tree.py*/



/****************************  DESCRIPTION  *****************************/
/*
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
*/



/****************************  EXAMPLES  *****************************/
/*
Example 1:
	Input: array = 1->2->3
	Output:
		 2  
		/ \
		1  3
		
Example 2:
	Input: 2->3->6->7
	Output:
		 3
		/ \
	       2   6
		     \
		      7

	Explanation:
	There may be multi answers, and you could return any of them.

*/



/****************************  CODE  *****************************/
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        # write your code here
        if not head:
            return None
        
        if not head.next:
            return TreeNode(head.val)
        
