"""***************************  TITLE  ****************************"""
"""920  Meeting Rooms.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
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
    def canAttendMeetings(self, intervals):
        if not intervals:
            return True
            
        if len(intervals) <= 1:
            return True
        
        intervals.sort(key=lambda x: x.start)
        
        end_time = intervals[0].end
        for idx in range(1, len(intervals)):
            if intervals[idx].start < end_time:
                return False
                
            end_time = intervals[idx].end
        
        return True
