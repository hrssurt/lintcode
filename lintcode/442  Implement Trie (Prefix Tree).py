"""***************************  TITLE  ****************************"""
"""442  Implement Trie (Prefix Tree).py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Implement a Trie with insert, search, and startsWith methods.
"""



"""***************************  EXAMPLES  ****************************"""
"""
insert
"""



"""***************************  CODE  ****************************"""
class Node:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Trie:
    
    def __init__(self):
        self.root = Node()

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        head = self.root
        for c in word:
            if c not in head.children:
                head.children[c] = Node()
            head = head.children[c]
        head.is_end = True

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        head = self.root
        for c in word:
            if c not in head.children:
                return False
            head = head.children[c]
        
        return head.is_end

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        head = self.root
        for c in prefix:
            if c not in head.children:
                return False
                
            head = head.children[c]
            
        return True
        

