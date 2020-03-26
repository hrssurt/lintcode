"""***************************  TITLE  ****************************"""
"""148. Sort List.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4


Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

"""



"""***************************  CODE  ****************************"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        mid = self.findMid(head)
        first, second = head, mid.next
        mid.next = None   # break the link
        
        l1 = self.sortList(first)
        l2 = self.sortList(second)
        return self.merge(l1, l2)
        
            
    def findMid(self, head):
        if not head or not head.next:
            return head
​
        slow, slow_cpy,  fast = head, head, head
        while fast and fast.next:
            fast = fast.next.next
            slow_cpy = slow
            slow = slow.next
​
        return slow_cpy
        
        
    def merge(self, l1, l2):
        head = dummy = ListNode("dummy")
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        while fast and fast.next:
​
