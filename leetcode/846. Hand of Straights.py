"""***************************  TITLE  ****************************"""
"""846. Hand of Straights.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

 




Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].

Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.

 

Note:


	1 <= hand.length <= 10000
	0 <= hand[i] <= 10^9
	1 <= W <= hand.length


"""



"""***************************  CODE  ****************************"""
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if not hand: return False
        if len(hand) % W != 0: return False
        
        d = Counter(hand)
        for card in sorted(hand):
            if d[card] > 0:
                for i in range(1, W):
                    target_card = card + i
                    if target_card not in d:
                        return False
                    
                    if d[target_card] < d[card]:
                        return False
                    
                    d[target_card] -= d[card]
                    
                d[card] = 0
        return True
​
