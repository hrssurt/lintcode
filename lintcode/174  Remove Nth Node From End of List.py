"""***************************  TITLE  ****************************"""
"""174  Remove Nth Node From End of List.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a linked list, remove the nth node from the end of list and return its head.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Example 1:
	Input: list = 1->2->3->4->5->null， n = 2
	Output: 1->2->3->5->null


Example 2:
	Input:  list = 5->4->3->2->1->null, n = 2
	Output: 5->4->3->1->null


"""



"""***************************  CODE  ****************************"""
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode("dummy")
        dummy.next = head
        slow, fast = dummy, head
        for _ in range(n):
            if fast:
                fast = fast.next
            else:
                return head  # n is greater than the length
                
        while fast:
            slow, fast = slow.next, fast.next
        
        slow.next = slow.next.next
        return dummy.next
        

