"""***************************  TITLE  ****************************"""
"""709. To Lower Case.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 


Example 1:

Input: "Hello"
Output: "hello"



Example 2:

Input: "here"
Output: "here"



Example 3:

Input: "LOVELY"
Output: "lovely"




"""



"""***************************  CODE  ****************************"""
class Solution:
    def toLowerCase(self, str: str) -> str:
        if not str: return str
        return str.lower()
        
​
