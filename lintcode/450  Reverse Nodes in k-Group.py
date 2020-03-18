"""***************************  TITLE  ****************************"""
"""450  Reverse Nodes in k-Group.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:
list = 1->2->3->4->5->null
k = 2
Output:
2->1->4->3->5

"""



"""***************************  CODE  ****************************"""
class Solution:
    def reverseKGroup(self, head, k):
        if not head or k <= 1:
            return head
        
        def reverse(head):
            new_head = None
            while head:
                rem = head.next
                head.next = new_head
                new_head = head
                head = rem

        def find_kth_node(head, k):   # define the kth node to the from, taking k steps, 
                                      # the node it stopped on
            for _ in range(k):
                if head:
                    head = head.next
                else:
                    return None
            return head
        
        dummy = ListNode("dummy")
        dummy.next = head
        cur = dummy
        while True:
            nk = find_kth_node(cur, k)    # cur -> n1 _> n2 -> nk
            if not nk:                    # we have less than k nodes left, no need to reverse
                break
            n1 = cur.next
            nkp1 = nk.next                # the k plus 1 node

            # reverse the net k nodes
            nk.next = None
            reverse(cur.next)
            cur.next = nk                 # cur-> nk -> nk-1 -> nk-2..... -> n1
            n1.next = nkp1                # connecting it back n1->nkp1
            
            # at this point, we have nk -> nk-1 -> nk-2 -> ... -> n1
            cur = n1
            
        return dummy.next    
            
            
                        
            
            
            
            
