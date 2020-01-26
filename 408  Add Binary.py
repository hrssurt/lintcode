"""***************************  TITLE  ****************************"""
"""408  Add Binary.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given two binary strings, return their sum (also a binary string).
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:
a = "0", b = "0"
Output:
"0"

"""



"""***************************  CODE  ****************************"""
class Solution:
    def addBinary(self, a, b):
        if not a:
            return b
        if not b:
            return a
        
        ia, ib, carry = len(a)-1, len(b)-1, 0
        ans = ""
        while ia >= 0 or ib >= 0:
            ta = int(a[ia]) if ia >= 0 else 0
            tb = int(b[ib]) if ib >= 0 else 0
            
            s = ta + tb + carry
            
            if s >= 2:
                carry = 1
            else:
                carry = 0
                
            s  %= 2
            ans = str(s) + ans
            ia, ib = ia - 1, ib -1
            
        if carry:
            ans = "1" + ans
        return ans            
                
        
