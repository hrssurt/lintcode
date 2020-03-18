"""***************************  TITLE  ****************************"""
"""1283  Reverse String.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Write a function that takes a string as input and returns the string reversed.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input："hello"
Output："olleh"

"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def reverseString(self, s):
        if not s:
            return s
            
        return "".join(reversed(s))

