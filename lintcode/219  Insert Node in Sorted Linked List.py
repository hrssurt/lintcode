"""***************************  TITLE  ****************************"""
"""219  Insert Node in Sorted Linked List.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Insert a node in a sorted linked list.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: head = 1->4->6->8->null, val = 5
Output: 1->4->5->6->8->null

"""



"""***************************  CODE  ****************************"""
class Solution:
    def insertNode(self, head, val):
        new_node = ListNode(val)
        if not head:
            return new_node
        elif val <= head.val:
            new_node.next = head
            return new_node
        elif not head.next:
            head.next = new_node
            return head
                
        else:
            left, right = head, head.next
            while right:
                if left.val <= val and right.val >= val:
                    left.next = new_node
                    new_node.next = right
                    return head
                else:
                    left, right = left.next, right.next
                    
            # the only way this loop breaks out and control goes here
            # is when val is greater than all the vals in nodes
            left.next = new_node
            return head
                
