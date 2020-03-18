"""***************************  TITLE  ****************************"""
"""217  Remove Duplicates from Unsorted List.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Write code to remove duplicates from an unsorted linked list.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: 1->2->1->3->3->5->6->3->null
Output: 1->2->3->5->6->null

"""



"""***************************  CODE  ****************************"""
class Solution:
    def removeDuplicates(self, head):
        
        if not head or not head.next:
            return head
        
        left, right = head, head.next
        seen = set([left.val])
        while right:
            if right.val in seen: # need to remove it from the list
                left.next = right.next
                right = right.next
            else:   # no need to remove, move two pointers forward
                seen.add(left.val)
                seen.add(right.val)
                left = left.next
                right = right.next
            
            
        return head
