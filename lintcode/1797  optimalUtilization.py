"""***************************  TITLE  ****************************"""
"""1797  optimalUtilization.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Give two sorted arrays. To take a number from each of the two arrays, the sum of the two numbers needs to be less than or equal to k, and you need to find the index combination with the largest sum of the two numbers. Returns a pair of indexes containing two arrays. If you have multiple index answers with equal sum of two numbers, you should choose the index pair with the smallest index of the first array.
"""



"""***************************  EXAMPLES  ****************************"""
"""
A = [1, 4, 6, 9], B = [1, 2, 3, 4], K = 9
return [2, 2]

"""



"""***************************  CODE  ****************************"""
class Solution:
    def optimalUtilization(self, A, B, K):
        if not A or not B:
            return []
        a, b = 0, len(B)-1
        best = [0, 0]
        while a < len(A) and b >= 0:
            # first, move the right index until the sum is smaller than the sum
            while (b >= 0 and A[a] + B[b] > K) or (b >= 1 and B[b] == B[b-1]):   # get rid of duplicates
                b -= 1
            
            if b < 0:      # this happens when both array numbers are so big
                break
            
            if A[a] + B[b] == K:
                return [a, b]
                
            else:  # sum is smaller than K when entering this flow
                   # update if we have found a better solution
                if A[a] + B[b] > A[best[0]] + B[best[1]]:
                    best = [a, b]
                    
                a += 1
        
        return best
