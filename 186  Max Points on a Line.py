"""***************************  TITLE  ****************************"""
"""186  Max Points on a Line.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:(1,2),(3,6),(0,0),(1,3).
Output:3

"""



"""***************************  CODE  ****************************"""
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
# y = mx + n
# m = (y1-y2) / (x1 - x2)
# n = (y2x1- y1x2) / (x1 - x2)

class Solution:
    def maxPoints(self, points):
        if not points:
            return 0
        if len(points) == 1:
            return 1
        
        max_count = 0
        for i, p1 in enumerate(points):
            x1, y1 = p1.x, p1.y
            d = {}       # used to store the count
            duplicate = 0
            for j in range(i+1, len(points)):
                x2, y2 = points[j].x, points[j].y
                dx, dy = x2-x1, y2-y1
                if dx == dy == 0:
                    duplicate += 1
                elif dx == 0:       # not dupllicate, but on the same vertical line
                    d['inf'] = d.get('inf', 0) + 1
                else:
                    d[dy/dx] = d.get(dy/dx, 0) + 1
            
            max_count = max(max_count, duplicate+1)     # in case its all duplicates in the llist
            for key, value in d.items():
                max_count = max(max_count, value+1+duplicate)   # add one to include the point itself, add dupllicate to 
            
                
        return max_count
            
                        
                        
                    
            
                    
                    
                

