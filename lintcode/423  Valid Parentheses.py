"""***************************  TITLE  ****************************"""
"""423  Valid Parentheses.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
"""



"""***************************  EXAMPLES  ****************************"""
"""
'(', ')'
"""



"""***************************  CODE  ****************************"""
class Solution:
    def isValidParentheses(self, s):
        stack = []
        open_p = set(["(", "[", "{"])
        close_p = set([")", "]", "}"])
        d = {"{": "}", "[": "]", "(": ")"}
        for char in s:
            if char in open_p:
                stack.append(char)
            elif char in close_p:
                if not len(stack):
                    return False
                o = stack.pop(-1)
                if d[o] != char:  # does not match
                    return False
        return len(stack) == 0

