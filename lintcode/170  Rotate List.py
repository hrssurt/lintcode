"""***************************  TITLE  ****************************"""
"""170  Rotate List.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a list, rotate the list to the right by k places, where k is non-negative.
"""



"""***************************  EXAMPLES  ****************************"""
"""
k
"""



"""***************************  CODE  ****************************"""
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or not k:
            return head
        
        slow, fast, l = head, head, 0
        while fast:
            fast = fast.next
            l += 1
        k %= l      # rotate length time is the same as not rotating
        if not k:
            return head
        
        fast = head
        for _ in range(k):
            fast = fast.next
        
        while fast.next:
            fast, slow = fast.next, slow.next
            
        new_head = slow.next
        slow.next = None
        fast.next = head    
        return new_head
    
        
        
        
        
            
    

