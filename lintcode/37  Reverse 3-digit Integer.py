"""***************************  TITLE  ****************************"""
"""37  Reverse 3-digit Integer.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Reverse a 3-digit integer.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: number = 123
Output: 321

"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        return number // 100  + number // 10 % 10 * 10 + number % 10 * 100

