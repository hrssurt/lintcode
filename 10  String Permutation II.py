"""***************************  TITLE  ****************************"""
"""10  String Permutation II.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a string, find all permutations of it without duplicates.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: "abb"
Output:
["abb", "bab", "bba"]

"""



"""***************************  CODE  ****************************"""
class Solution:
    def stringPermutation2(self, str):
        def dfs(lst):
            if not lst:
                return [""]
            elif len(lst) == 1:
                return [lst]
            else:
                result = []
                for i, e in enumerate(lst):
                    if i >= 1 and lst[i] == lst[i-1]:
                        continue
                    rest = lst[:i] + lst[i+1:]
                    permuations = dfs(rest)
                    for p in permuations:
                        result.append([e] + p)
                return result
        if not str:
            return [""]
        lst = sorted(str)
        result = dfs(lst)
        return ["".join(l) for l in result]

