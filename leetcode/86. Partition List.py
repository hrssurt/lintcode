"""***************************  TITLE  ****************************"""
"""86. Partition List.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5


"""



"""***************************  CODE  ****************************"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        d1 = before = ListNode("Dummy")
        d2 = after = ListNode("Dummy")
        
        while head:
            if head.val < x:
                before.next = head
                before = head        
            else:
                after.next = head
                after = head
                
            head = head.next
        after.next = None       # this line is important
        before.next = d2.next
        return d1.next            
        
​
