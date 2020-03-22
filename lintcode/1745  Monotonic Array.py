"""***************************  TITLE  ****************************"""
"""1745  Monotonic Array.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
要么递增，要么递减。用一个 OR
"""



"""***************************  EXAMPLES  ****************************"""
"""
    for i in range(1, len(A)):
        if A[i] < A[i-1]:
            increasing = False
        elif A[i] > A[i-1]:
            decreasing = False
    return decreasing or increasing
"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param A: a array
    @return: is it monotonous
    """
    def isMonotonic(self, A):
        # Write your code here.
        
        increasing, decreasing = True, True
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                increasing = False
            elif A[i] > A[i-1]:
                decreasing = False
                
        return increasing or decreasing
