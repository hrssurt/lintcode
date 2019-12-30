"""***************************  TITLE  ****************************"""
"""166  Nth to Last Node in List.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Find the nth to last element of a singly linked list. 
"""



"""***************************  EXAMPLES  ****************************"""
"""
Example 1:
	Input: list = 3->2->1->5->null, n = 2
	Output: 1


Example 2:
	Input: list  = 1->2->3->null, n = 3
	Output: 1


"""



"""***************************  CODE  ****************************"""
class Solution:
    def nthToLast(self, head, n):
        slow, fast = head, head
        for _ in range(n):
            fast = fast.next
            
        while fast:
            slow, fast = slow.next, fast.next
            
        return slow
            
            

