"""***************************  TITLE  ****************************"""
"""1812  Rotation Number.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Give you a positive integer n,  Rotations Number is a number that rotates by 180° after each digit, and is not equal to its own number. And you also ensure that the number of rotations is less than or equal to n. You should find all the numbers that satisfy the definition of the Rotation Number in the range of 1 - n and return an array res. For example, 8069->8096, 769 cannot be rotated because 7 is not a number after 180° rotation
"""



"""***************************  EXAMPLES  ****************************"""
"""
res
"""



"""***************************  CODE  ****************************"""
class Solution:
    def RotationNumber(self, n):
        cannot_rotate = set([str(i) for i in range(0,10)]) - set(["0","6","8","9"])
        d = {"0": "0", "6": "9", "8": "8", "9": "6"}
        def rotate(n, bound):
            result = []
            for char in str(n):
                if char in cannot_rotate:
                    return None
                result.append(d[char])
                
            new = int("".join(result)) 
            if  new != n and new <= bound:
                return n
            else:
                return None
        result = []    
        for i in range(1, n+1):
            r = rotate(i, n)
            if r:
                result.append(r)
        return result
            

