"""***************************  TITLE  ****************************"""
"""206. Reverse Linked List.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL


Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

"""



"""***************************  CODE  ****************************"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        while head:
            rem = head.next
            head.next = new_head
            new_head = head
            head = rem
            
        return new_head
        
​
