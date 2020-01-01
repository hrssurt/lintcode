"""***************************  TITLE  ****************************"""
"""451  Swap Nodes in Pairs.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a linked list, swap every two adjacent nodes and return its head.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: 1->2->3->4->null
Output: 2->1->4->3->null

"""



"""***************************  CODE  ****************************"""
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        left, right = head, head.next
        while left and right:
            left.val, right.val = right.val, left.val
            if right.next:
                left = right.next
                right = right.next.next
            else:
                break
            
        return head

