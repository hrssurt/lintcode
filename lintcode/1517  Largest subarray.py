"""***************************  TITLE  ****************************"""
"""1517  Largest subarray.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a array A consisting of N integers and an integer K,
return the largest contiguous subarray from all the contiguous subarrays of length K.
We defined that subarray A is greater than subarray B if the first non-matching element in both arrays has a greater value in A than in B.
For example,A=[1,2,4,3],B=[1,2,3,5].
A is greater than B because A[2]>B[2].
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:
[1,4,3,2,5]
4
Output:
[4,3,2,5]
Explanation:
there are two subarrays of size 4:
[1,4,3,2]and [4,3,2,5].
So the largest subarray is [4,3,2,5].

"""



"""***************************  CODE  ****************************"""
class Solution:
    def largestSubarray(self, A, K):
        if K > len(A):
            return []
            
        def is_greater(X, Y):
            for a,b in zip(X,Y):
                if a > b:
                    return True
                elif a < b:
                    return False
                else:
                    continue
            return True
            
        start, end = 0, K-1
        max_array = A[start: end+1]
        while end < len(A):
            candidate = A[start: end+1]
            if is_greater(candidate, max_array):
                max_array = candidate
            
            start += 1
            end += 1
        return max_array
            
