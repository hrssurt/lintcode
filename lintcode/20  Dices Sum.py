"""***************************  TITLE  ****************************"""
"""20  Dices Sum.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Throw n dices, the sum of the dices' faces is S. Given n, find the all possible value of S along with its probability.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: n = 1
Output: [[1, 0.17], [2, 0.17], [3, 0.17], [4, 0.17], [5, 0.17], [6, 0.17]]
Explanation: Throw a dice, the sum of the numbers facing up may be 1, 2, 3, 4, 5, 6, and the probability of each result is 0.17.

"""



"""***************************  CODE  ****************************"""
class Solution:
    def dicesSum(self, n):
        d = {}
        
        def times(n, s):  # using n dices to get sum s, returns the number of compositions to             get that
            if (n,s) in d:
                return d[(n,s)]
                
            elif n == 1:
                if 1 <= s <= 6:
                    d[(1, s)] = 1
                    return 1
                else:
                    return 0
            else:
                acc = 0
                for k in range(1, 7):
                    if s-k > 0:     # s has to be greater than k as the sum only increases                                         # after adding a new dice 
                        acc += times(n-1, s - k) # using 1 less dice to get 
                d[(n, s)] = acc
                return acc
                
        lst = [(i, times(n, i)) for i in range(n, 6*n+1)]
        s = sum([k[1] for k in lst])
        lst = [(n, k / s) for n,k in lst]
        return lst
        
        
