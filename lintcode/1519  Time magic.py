"""***************************  TITLE  ****************************"""
"""1519  Time magic.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
In Hogwarts School of Magic, there is a simple time magic that converts the current time to the maximum time, but only a few fixed positions. The longest time is 23:59 and the shortest time is 00:00. The format of the time is hh:mm
For example: now is "2?:2?", then the maximum time that can be converted is "23:29"
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:  "?4:5?"
Output: "14:59"
Explanation: Return maximum time.

"""



"""***************************  CODE  ****************************"""
class Solution:
    def timeMagic(self, newTime):
        if "?" not in newTime:
            return newTime
        result = []
        for idx, c in enumerate(newTime):
            if c == "?":
                if idx == 0 and newTime[1] == '?':
                    result.append("2")
                elif idx == 0 and newTime[1] <= '3':
                    result.append("2")
                elif idx == 0 and newTime[1] >= '3':
                    result.append("1")
                elif idx == 1 and (result[0] == '1' or result[0] == '0'):
                    result.append("9")
                elif idx == 1 and result[0] == '2':
                    result.append('3')
                elif idx == 3:
                    result.append('5')
                elif idx == 4:
                    result.append('9')
            else:
                result.append(c)
                
        return ''.join(result)
