/****************************  TITLE  *****************************/
/*165  Merge Two Sorted Lists.java*/



/****************************  DESCRIPTION  *****************************/
/*
Merge two sorted (ascending) linked lists and return it as a new sorted list. The new sorted list should be made by splicing together the nodes of the two lists and sorted in ascending order.
*/



/****************************  EXAMPLES  *****************************/
/*
Example 1:
	Input: list1 = null, list2 = 0->3->3->null
	Output: 0->3->3->null


Example 2:
	Input:  list1 =  1->3->8->11->15->null, list2 = 2->null
	Output: 1->2->3->8->11->15->null


*/



/****************************  CODE  *****************************/
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        }
        if (l2 == null) {
            return l1;
        }
        ListNode dummy = new ListNode(-1);
        ListNode end = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                end.next = l1;
                l1 = l1.next;
                end = end.next;
            } else {
                end.next = l2;
                l2 = l2.next;
                end = end.next;
            } 
        }
        
        while (l1 != null) {
            end.next = l1;
            l1 = l1.next;
            end = end.next;
        }
        
        while (l2 != null) {
            end.next = l2;
            l2 = l2.next;
            end = end.next;
        }
        
        return dummy.next;
    }
}
