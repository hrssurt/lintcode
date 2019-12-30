"""***************************  TITLE  ****************************"""
"""113  Remove Duplicates from Sorted List II.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

"""



"""***************************  EXAMPLES  ****************************"""
"""
Input : 1->2->3->3->4->4->5->null
Output : 1->2->5->null

"""



"""***************************  CODE  ****************************"""
        
        dummy = ListNode("dummy")
        dummy.next = head
        left, right = dummy, head
        
        while right:
            duplicate_flag = False
            while right.next and right.val == right.next.val:
                right = right.next
                duplicate_flag = True
                
            # when the loop break out, and flag is true 
            # right will be the last node of the duplicates
            
            if duplicate_flag:
                left.next = right.next
            else:
                left = left.next
                
            
            if right:
                right = right.next
                    
        return dummy.next
            
            
                

