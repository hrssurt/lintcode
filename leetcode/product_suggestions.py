
# Title: 1268. Search Suggestions System

# Description
"""
Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 
"""

# Example
"""
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]


Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
"""

#############################################################

class Node:
    def __init__(self):
        self.children = {}
        self.words = []  # words that start with the prefix
        self.is_end = False

class Trie:
    def __init__(self, k = 3):
        self.root = Node()   # dummy node
        self.k = k
        
    def insert(self, word):
        head = self.root
        for c in word:
            if c not in head.children:
                head.children[c] = Node()
            
            head = head.children[c]
            if len(head.words) < 3:
                head.words.append(word)
                
        head.is_end = True
                
    
    def search(self, prefix):
        head = self.root
        res = []
        for c in prefix:
            if c not in head.children:
                break
            head = head.children[c]
            res.append(head.words)
        while len(res) < len(prefix):
            res.append([])
            
        return res
            
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        t = Trie()
        for product in products:
            t.insert(product)
            
        return t.search(searchWord)
            
        