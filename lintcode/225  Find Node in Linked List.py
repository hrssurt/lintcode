"""***************************  TITLE  ****************************"""
"""225  Find Node in Linked List.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Find a node with given value in a linked list. Return null if not exists.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:  1->2->3 and value = 3
Output: The last node.

"""



"""***************************  CODE  ****************************"""
class Solution:
    def findNode(self, head, val):
        while head:
            if head.val == val:
                return head
            else:
                head = head.next
                
        return None
