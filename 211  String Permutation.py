"""***************************  TITLE  ****************************"""
"""211  String Permutation.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given two strings, write a method to decide if one is a permutation of the other.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Example 1:
	Input:  "abcd", "bcad"
	Output:  True


Example 2:
	Input: "aac", "abc"
	Output:  False


"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """
    def Permutation(self, A, B):
        if not A and not B:
            return True
            
        if not A or not B or len(A) != len(B):
            return False
            
        d1, d2 = {}, {}
        for i in range(len(A)):
            char_a = A[i]
            char_b = B[i]
            d1[char_a] = d1.get(char_a, 0) + 1
            d2[char_b] = d2.get(char_b, 0) + 1
            
        for char, count in d1.items():
            if char not in d2 or d2[char] != d1[char]:
                return False
                
        return True
        
        

