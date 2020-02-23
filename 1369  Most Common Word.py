"""***************************  TITLE  ****************************"""
"""1369  Most Common Word.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:  paragraph = "Bob hit a ball, the hit BALL flew far after it was hit." and banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

"""



"""***************************  CODE  ****************************"""
import string
class Solution:
    """
    @param paragraph: 
    @param banned: 
    @return: nothing
    """
    def mostCommonWord(self, paragraph, banned):
        if not paragraph:
            return ""
        p = paragraph.translate(str.maketrans('', '', string.punctuation))
        p = p.lower()
        words = [word for word in p.split() if word not in banned]
        d = {}
        max_count, max_word = -1, ""
        for word in words:
            d[word] = d.get(word, 0) + 1
            if d[word] > max_count:
                max_word = word
                max_count = d[word]
                
        return max_word
