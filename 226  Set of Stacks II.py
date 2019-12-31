"""***************************  TITLE  ****************************"""
"""226  Set of Stacks II.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack). SetOfStacks.popAt(int index) which performs a pop operation on a specific sub-stack.If we pop an element from stack 1, we need to remove the bottom of stack 2 and push it onto stack 1. We then need to rollover from stack 3 to stack 2, stack 4 to stack 3, etc.
"""



"""***************************  EXAMPLES  ****************************"""
"""
SetOfStacks
"""



"""***************************  CODE  ****************************"""
class SetOfStacks2:
    """
    @param: capacity: an inetger, capacity of sub stack
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.data = []

    """
    @param: v: An integer
    @return: nothing
    """
    def push(self, v):
        # write your code here
        self.data.insert(0, v)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        return self.data.pop(0)

    """
    @param: index: The index of a specific sub-stack
    @return: top element of the specific sub-stack
    """
    def popAt(self, index):
        # write your code here
        return self.data.pop(-(index+1)*self.capacity) if (index+1)*self.capacity <= len(self.data) else self.pop()

