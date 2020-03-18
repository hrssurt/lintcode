"""***************************  TITLE  ****************************"""
"""380  Intersection of Two Linked Lists.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Write a program to find the node at which the intersection of two singly linked lists begins.
"""



"""***************************  EXAMPLES  ****************************"""
"""
null
"""



"""***************************  CODE  ****************************"""
class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        
        def get_len(head):
            len = 0
            while head:
                len += 1
                head = head.next
            return len
            
        def walk_k_steps(head, k):
            for _ in range(k):
                head = head.next
            return head
            
        len_a = get_len(headA)
        len_b = get_len(headB)
        
        if len_a > len_b:
            headA = walk_k_steps(headA, len_a-len_b)
        else:
            headB = walk_k_steps(headB, len_b-len_a)
        
        # now they are at the same page for headA AND headB
        while headA and headB:
            if headA is headB:
                return headA
            else:
                headA, headB = headA.next, headB.next
        return None
            
