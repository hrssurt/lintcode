"""***************************  TITLE  ****************************"""
"""223  Palindrome Linked List.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Implement a function to check if a linked list is a palindrome.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: 1->2->1
output: true

"""



"""***************************  CODE  ****************************"""
class Solution:
    def isPalindrome(self, head):
        def find_mid(head):
            if not head or not head.next:
                return head
            else:
                slow, fast = head, head
                while fast.next and fast.next.next:
                    slow, fast = slow.next, fast.next.next
                    
                return slow
    
        def reverse(head):
            new_head = None
            while head:
                rem = head.next
                head.next = new_head
                new_head = head
                head = rem
            return new_head
            
        if not head or not head.next:
            return True
            
        mid = find_mid(head)
        second = reverse(mid.next)
        mid.next = None
        while second and head:
            if second.val == head.val:
                second, head = second.next, head.next
            else:
                return False
        return True

