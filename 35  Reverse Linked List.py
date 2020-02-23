"""***************************  TITLE  ****************************"""
"""35  Reverse Linked List.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Reverse a linked list.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: 1->2->3->null
Output: 3->2->1->null

"""



"""***************************  CODE  ****************************"""
class Solution:
    def reverse(self, head):
        if not head:
            return head
            
        new_head = None
        while head:
            rem = head.next
            head.next = new_head
            new_head = head
            head = rem
                
        return new_head                
        

