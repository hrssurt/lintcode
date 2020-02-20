"""***************************  TITLE  ****************************"""
"""471  Top K Frequent Words.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a list of words and an integer k, return the top k frequent words in the list.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:
  [
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"
  ]
  k = 3
Output: ["code", "lint", "baby"]

"""



"""***************************  CODE  ****************************"""
import heapq

class Word:
    def __init__(self, word, count):
        self.word, self.count = word, count
        
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
            
        return self.count < other.count
        
    def __gt__(self, other):
        if self.count == other.count:
            return self.word < other.word
        return self.count > other.count
        
    def __eq__(self, other):
        return self.count == other.count and self.word == other.word


class Solution:

    
    
    def topKFrequentWords(self, words, k):
        if not words or k <= 0:
            return []
            
        if k >= len(words):
            return words
        
        d, q = {}, []
        for word in words:
            d[word] = d.get(word, 0) + 1
        
        
        for word, count in d.items():
            if len(q) < k:
                heapq.heappush(q, Word(word, count))
            elif q[0] < Word(word, count):
                heapq.heappop(q)
                heapq.heappush(q, Word(word, count))
            
        return [i.word for i in sorted(q, reverse=True)]
        
            
