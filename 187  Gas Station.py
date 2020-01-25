"""***************************  TITLE  ****************************"""
"""187  Gas Station.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
"""



"""***************************  EXAMPLES  ****************************"""
"""
gas[i]
"""



"""***************************  CODE  ****************************"""
class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        
        remain = 0
        final_idx = 0
        for idx in range(len(gas)):
            temp = remain + gas[idx] - cost[idx]
            if temp < 0:
                remain = 0
                final_idx = idx + 1
            else:
                remain = temp
                
        return final_idx
                

