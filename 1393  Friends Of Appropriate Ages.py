"""***************************  TITLE  ****************************"""
"""1393  Friends Of Appropriate Ages.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.

"""



"""***************************  CODE  ****************************"""
class Solution:
    def numFriendRequests(self, ages):
        def if_request(a, b):
            return not (b <= 0.5 * a + 7 or b > a or b > 100 and a < 100) 
        d = {}
        for age in ages:
            d[age] = d.get(age, 0) + 1
        result = 0
        for age_a, count_a in d.items():
            for age_b, count_b in d.items():
                if age_a != age_b and if_request(age_a, age_b):
                    result += count_a * count_b
                elif age_a == age_b and if_request(age_a, age_a):
                    result += count_a * (count_a - 1)
        return result
        
        

