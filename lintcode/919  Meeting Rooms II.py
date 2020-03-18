"""***************************  TITLE  ****************************"""
"""919  Meeting Rooms II.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
"""



"""***************************  EXAMPLES  ****************************"""
"""
[[s1,e1],[s2,e2],...] (si < ei)
"""



"""***************************  CODE  ****************************"""
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
            
        times = []
        for i in intervals:
            times.append((i.start, 1))
            times.append((i.end, -1))
        
        times.sort()
        
        max_count, count = 0, 0
        for t, c in times:
            count += c
            max_count = max(max_count, count)
            
        return max_count

