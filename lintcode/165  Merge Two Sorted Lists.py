"""***************************  TITLE  ****************************"""
"""165  Merge Two Sorted Lists.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Merge two sorted (ascending) linked lists and return it as a new sorted list. The new sorted list should be made by splicing together the nodes of the two lists and sorted in ascending order.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Example 1:
	Input: list1 = null, list2 = 0->3->3->null
	Output: 0->3->3->null


Example 2:
	Input:  list1 =  1->3->8->11->15->null, list2 = 2->null
	Output: 1->2->3->8->11->15->null


"""



"""***************************  CODE  ****************************"""
class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode("dummy")
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        return dummy.next
        
        

