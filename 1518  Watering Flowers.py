"""***************************  TITLE  ****************************"""
"""1518  Watering Flowers.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
You and your friend are gardeners,and you take care of your plants.The plants are planted in a row, and each of them needs a specific amount of water.You are about to water them using watering cans.To avoid mistakes like applying too much water,or not watering a plant at all,you have decided to:
** water the plants in the order in which they appear:you will water from left to right,and your friend will water from right to left;**
** water each plant if you have sufficient water for it,otherwise refill your watering can;**
** water each plant in one go,i.e. withoua  taking a break to refill the watering can in the middle of watering a single plant.This means that you may sometimes have to refill your watering can before or after watering a plant,even though it's not completely empty.**
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input：[2,4,5,1,2],5,7
Output：3
Explanation：First you refill and water plants[0] and simultaneously your friend refills and waters plants[4].Then you refill and water plants[1] and simultaneously your friend waters plants[3].Finally you water plants[2] togerther (as together you have exactly 5 units of water).

"""



"""***************************  CODE  ****************************"""
class Solution:
    def waterPlants(self, plants, capacity1, capacity2):
        if not plants: return 0
        left, right = 0, len(plants) - 1
        can1, can2 = 0, 0
        refill_count = 0
        while left < right:
            if plants[left] > can1:
                refill_count += 1
                can1 = capacity1 - plants[left]
            else:
                can1 -= plants[left]
            
            if plants[right] > can2:
                refill_count += 1
                can2 = capacity2 - plants[right]
            else:
                can2 -= plants[right]
                
            left, right = left + 1, right - 1
        
        if left == right: # meet
            if can1 + can2 < plants[left]:
                refill_count += 1
                
        return refill_count
