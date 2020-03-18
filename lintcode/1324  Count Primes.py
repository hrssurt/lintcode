"""***************************  TITLE  ****************************"""
"""1324  Count Primes.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Count the number of prime numbers less than a non-negative number, n.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: n = 2
Output: 0

"""



"""***************************  CODE  ****************************"""
import math
class Solution:
    def countPrimes(self, n):
        deleted = [False for _ in range(0, n)]
        count = 0
        for idx in range(2, n):
            if not deleted[idx]:
                # this idx is a new prime
                new_prime = idx
                count += 1
                deleted[idx] = True
                while idx < n:
                    deleted[idx] = True
                    idx += new_prime
                    
        
            
        return count

