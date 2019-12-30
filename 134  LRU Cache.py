"""***************************  TITLE  ****************************"""
"""134  LRU Cache.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.
"""



"""***************************  EXAMPLES  ****************************"""
"""
get
"""



"""***************************  CODE  ****************************"""
# use a double linked list 
# use a double linked list 
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.d = {}         # stores {key: Node}
        self.head = Node("dummy", "dummy")
        self.tail = Node("dummy2", "dummy2")
        self.head.next = self.tail
        self.tail.prev = self.head

    """
    @param: key: An integer
    @return: An integer
    """
    def move_to_tail(self, val):
        target_node = self.d[val]
        if target_node is self.tail.prev:   # already in the end
            return

        prev_node = target_node.prev
        next_node = target_node.next
        
        # get target_node out of the chain
        prev_node.next = next_node
        next_node.prev = prev_node
        
        # put target_node on the back
        rem = self.tail.prev
        self.tail.prev = target_node
        target_node.next = self.tail
        target_node.prev = rem
        rem.next = target_node
        
            
        
    
    def get(self, key):
        # write your code here
        if key not in self.d:
            return -1
        
        self.move_to_tail(key)
        return self.d[key].val
        

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.d:
            self.d[key].val = value
            self.move_to_tail(key)
        else:   # key is not present, two cases:
                # one is capacity full
                # one is capacity not full
            if len(self.d) < self.capacity:
                new_node = Node(key, value)
                self.d[key] = new_node
                
                # add new key to end, update capacity
                rem = self.tail.prev
                rem.next = new_node
                new_node.prev = rem
                self.tail.prev = new_node
                new_node.next = self.tail
            else:
                # capacity full, we need to remove the least recent one
                # which is just the head of the 
                remove_node = self.head.next
                re_next = remove_node.next
                self.head.next = re_next
                re_next.prev = self.head
                del self.d[remove_node.key]
                
                
                # append the new node to end
                # no need to change capacity as we are full
                new_node = Node(key, value)
                self.d[key] = new_node
                
                rem = self.tail.prev
                rem.next = new_node
                new_node.prev = rem
                self.tail.prev = new_node
                new_node.next = self.tail
    
        

            