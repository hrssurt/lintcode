"""***************************  TITLE  ****************************"""
"""977. Squares of a Sorted Array.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 


Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]



Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]


 

Note:


	1 <= A.length <= 10000
	-10000 <= A[i] <= 10000
	A is sorted in non-decreasing order.



"""



"""***************************  CODE  ****************************"""
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return []
        
        p = 0
        while p < len(A) and A[p] <= 0:
            p += 1
            
        n = p - 1           # positive pointer and negative pointer
        
        res = []
        while p >= 0 and n >= 0 and p < len(A) and n < len(A):
            if abs(A[n]) < abs(A[p]):
                res.append(A[n] ** 2)
                n -= 1
            else:
                res.append(A[p] ** 2)
                p += 1
                
        
        while p < len(A):
            res.append(A[p] ** 2)
            p+=1
            
        while n >= 0:
            res.append(A[n] ** 2)
            n-=1
        return res
        
        
​
