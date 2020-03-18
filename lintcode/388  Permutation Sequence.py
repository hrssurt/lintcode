"""***************************  TITLE  ****************************"""
"""388  Permutation Sequence.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given n and k, find the kth permutation of the dictionary order in the full permutation of n.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: n = 3, k = 4
Output: "231"
Explanation:
For n = 3, all permutations are listed as follows:
"123", "132", "213", "231", "312", "321"

"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param n: n
    @param k: the k th permutation
    @return: return the k-th permutation
    """
    def getPermutation(self, n, k):
        if not n:
            return ""
        # write your code here
        def dfs(lst):
            if not lst:
                return []
            elif len(lst) == 1:
                return [lst]
            else:
                result = []
                for i in range(len(lst)):
                    e = lst[i]
                    rest = lst[:i] +  lst[i+1:]
                    permutations = dfs(rest)
                    for p in permutations:
                        result.append([e] + p)
                return result
                
        result = dfs([str(i) for i in range(1,n+1)])
        return "".join(result[k-1])

