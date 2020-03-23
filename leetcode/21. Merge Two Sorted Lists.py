"""***************************  TITLE  ****************************"""
"""21. Merge Two Sorted Lists.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4


"""



"""***************************  CODE  ****************************"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = cur = ListNode("dummy")
        
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
            
            
        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
            
        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next
            
        return dummy_head.next
​
