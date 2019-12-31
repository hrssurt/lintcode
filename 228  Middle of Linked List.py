"""***************************  TITLE  ****************************"""
"""228  Middle of Linked List.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Find the middle node of a linked list.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:  1->2->3
Output: 2	
Explanation: return the value of the middle node.

"""



"""***************************  CODE  ****************************"""
class Solution:
    def middleNode(self, head):
        # write your code here
        if not head or not head.next:
            return head
            
        fast, slow = head, head
        while fast and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        
        return slow
