"""***************************  TITLE  ****************************"""
"""1808  Minimum Domino Rotations For Equal Row.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
"""



"""***************************  EXAMPLES  ****************************"""
"""
Example1:
Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

"""



"""***************************  CODE  ****************************"""
            for i in A:
                if i != A[0]:
                    return False
            return True
                
                
        
        def dfs(A, B, idx):
            if idx == len(A):
                if all_same(A) or all_same(B):
                    return 0
                else:
                    return float('inf')
            else:
                if A[idx] == B[idx]:
                    return dfs(A, B, idx+1)
                else:
                    x1 = dfs(A, B, idx+1)
                    A[idx], B[idx] = B[idx], A[idx]
                    x2 = dfs(A, B, idx+1) + 1
                    A[idx], B[idx] = B[idx], A[idx]
                    return min(x1, x2)
        if not A: return 0
        r = dfs(A, B, 0)
        if r == float('inf'):
            return -1
        return r
            

