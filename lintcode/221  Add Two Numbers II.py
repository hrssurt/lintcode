"""***************************  TITLE  ****************************"""
"""221  Add Two Numbers II.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
You have two numbers represented by linked list, where each node contains a single digit. The digits are stored in forward order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
"""



"""***************************  EXAMPLES  ****************************"""
"""
forward
"""



"""***************************  CODE  ****************************"""
class Solution:
    def addLists2(self, l1, l2):
        def reverse(head):
            new_head = None
            while head:
                rem = head.next
                head.next = new_head
                new_head = head
                head = rem
            return new_head
            
        def add(l1,l2):
            carry, s = 0, 0
            dummy = ListNode("dummy")
            cur = dummy
            while l1 or l2 or carry:
                s = 0
                if l1:
                    s += l1.val
                    l1 = l1.next
                if l2:
                    s += l2.val
                    l2 = l2.next
                s += carry
                carry = s // 10
                s %= 10
                new_node = ListNode(s)
                cur.next = new_node
                cur = new_node
            return dummy.next
            
        return reverse(add(reverse(l1), reverse(l2)))
                
