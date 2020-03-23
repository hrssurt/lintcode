"""***************************  TITLE  ****************************"""
"""234. Palindrome Linked List.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false

Example 2:

Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?

"""



"""***************************  CODE  ****************************"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        
        def find_mid(head):
            slow = fast = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        
        
        def reverse(head):
            new_head = None
            while head:
                rem = head.next
                head.next = new_head
                new_head = head
                head = rem
                
            return new_head
        
        
        first, second = head, reverse(find_mid(head))   # first represents first half, second represents second half
        while first and second:
            if first.val != second.val:
                return False
            
            first, second = first.next, second.next
            
        return True
        
​
