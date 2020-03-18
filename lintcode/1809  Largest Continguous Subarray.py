"""***************************  TITLE  ****************************"""
"""1809  Largest Continguous Subarray.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given array A and length K, return a contiguous subarray of maximum length K, for example A = [6,6,2,9,7,6], K = 5, a total of two subarray a = [6, 6,2,9,7],b = [6,2,9,7,6], the first array is larger than the second array because they are not equal when the index is 1, and a [1] > b [ 1]. So return the first array.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Example:
Input:
A = [3,6,2,9,7,6]
K = 5
Output: [6,2,9,7,6]
Explaintation:
There are two subarray[3,6,2,9,7] and [6,2,9,7,6],because 6 > 3 ,you should return  [6,2,9,7,6]

"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param A: A Integer array
    @param K: a integer
    @return: a contiguous array of maximum length K
    """
    def LargestContinguousSubarray(self, A, K):
        if K > len(A):
            return []
        def compare(a_start, b_start, K, A):
            # return 1 if a_start is greater than b_start
            # return 0 otherwise
            for i in range(K):
                if A[a_start+i] > A[b_start+i]:
                    return 1
                elif A[a_start+i] < A[b_start+i]:
                    return 0
                
            return 1
        
        cur_max_start = 0
        
        for start in range(0, len(A)-K+1, 1):
            if compare(start, cur_max_start, K, A):
                cur_max_start = start
        
        return A[cur_max_start: cur_max_start+K]
                
        
