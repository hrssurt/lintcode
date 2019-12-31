"""***************************  TITLE  ****************************"""
"""173  Insertion Sort List.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Sort a linked list using insertion sort.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Example 1:
	Input: 0->null
	Output: 0->null


Example 2:
	Input:  1->3->2->0->null
	Output :0->1->2->3->null
	


"""



"""***************************  CODE  ****************************"""
class Solution:
    def insertionSortList(self, head):
        cur = head # if marks the place where stuff before cur are already sorted
        while cur:
            tail = cur
            while tail:
                if tail.val < cur.val:
                    tail.val, cur.val = cur.val, tail.val   # python swap
                else:
                    tail = tail.next
            cur = cur.next
                    
            
        return head

