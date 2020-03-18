"""***************************  TITLE  ****************************"""
"""112  Remove Duplicates from Sorted List.py"""



"""***************************  DESCRIPTION  ****************************"""
"""

Given a sorted linked list, delete all duplicates such that each element appear only once.

"""



"""***************************  EXAMPLES  ****************************"""
"""
Example 1:
	Input:  null
	Output: null


Example 2:
	Input:  1->1->2->null
	Output: 1->2->null
	
Example 3:
	Input:  1->1->2->3->3->null
	Output: 1->2->3->null
	


"""



"""***************************  CODE  ****************************"""

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if not head or not head.next:
            return head
        
        
        left, right = head, head.next
        
        while right:
            if left.val == right.val:
                # skip
                left.next = right.next
                # does not need to move left, only move right
                right = right.next
            else:
                left, right = left.next, right.next
                
        return head