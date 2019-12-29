/****************************  TITLE  *****************************/
/*105  Copy List with Random Pointer.py*/



/****************************  DESCRIPTION  *****************************/
/*
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
*/



/****************************  EXAMPLES  *****************************/
/*

*/



/****************************  CODE  *****************************/
"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        # first create the nodes
        if not head:
            return None
        
        dummy = RandomListNode("dummy")
        cur = dummy
        d = {}      # key old reference, value new reference of the equivalent node
        while head:
            new_node = RandomListNode(head.label)
            d[head] = new_node             # record the equivalent
            new_node.random = head.random  # for now, just copy the value
            cur.next = new_node
            cur = cur.next
            head = head.next
