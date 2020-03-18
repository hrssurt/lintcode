"""***************************  TITLE  ****************************"""
"""1016  Minimum Swaps To Make Sequences Increasing.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
∵一定有解
∴要么A[i] > A[i-1],  B[i] > B[i-1]即两条平行上升线，要么是B[i] > A[i-1], A[i] > B[i-1]即前一种情况把A[i]B[i]换一下
"""



"""***************************  EXAMPLES  ****************************"""
"""
A
"""



"""***************************  CODE  ****************************"""
class Solution:
    def minSwap(self, A, B):
        if not A: return 0
        keep = [float('inf') for _ in range(len(A))]
        swap = [float('inf') for _ in range(len(B))]
        
        keep[0] = 0   # The number of swaps needed to get the required order if we dont                       # swap [0:0] inclusive
        swap[0] = 1   # The number of swaps needed to get the required order if we swap
                      # the 0 position to get [0:0] inclusive
        for i in range(1, len(A)):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                keep[i] = keep[i-1]
                swap[i] = swap[i-1] + 1
            if A[i] > B[i-1] and B[i] > A[i-1]:
                keep[i] = min(swap[i-1], keep[i])
                swap[i] = keep[i-1]+1
        
        return min(keep[len(A)-1], swap[len(A)-1])
            

