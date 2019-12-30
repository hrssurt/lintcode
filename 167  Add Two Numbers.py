"""***************************  TITLE  ****************************"""
"""167  Add Two Numbers.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
"""



"""***************************  EXAMPLES  ****************************"""
"""
reverse
"""



"""***************************  CODE  ****************************"""
class Solution:
    def addLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
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
            
            

