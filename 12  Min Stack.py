"""***************************  TITLE  ****************************"""
"""12  Min Stack.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Implement a stack with following functions:
"""



"""***************************  EXAMPLES  ****************************"""
"""
push(val)
"""



"""***************************  CODE  ****************************"""
class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        if not len(self.stack):
            self.stack.append((number, number))  # val, min_val
        else:
            new_min_val = min(self.stack[-1][1], number)
            self.stack.append((number, new_min_val))

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        return self.stack.pop(-1)[0]

    """
    @return: An integer
    """
    def min(self):
        # write your code here
        return self.stack[-1][1]

