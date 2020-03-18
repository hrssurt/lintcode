"""***************************  TITLE  ****************************"""
"""230  Animal Shelter.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
An animal shelter holds only dogs and cats, and operates on a strictly "first in, first out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog and dequeueCat.
"""



"""***************************  EXAMPLES  ****************************"""
"""
dogs
"""



"""***************************  CODE  ****************************"""

class Node:
    def __init__(self, name, timestamp, next=None):
        self.name, self.timestamp, self.next = name, timestamp, next

class AnimalShelter:
    def __init__(self):
        self.dog, self.cat = Node('dummy', "dummy"), Node('dummy', 'dummy')
        self.CAT, self.DOG = 0, 1
        self.timestamp = 0
    def enqueue(self, name, type):
        if type == self.DOG:
            cur = self.dog
        else:
            cur = self.cat
        while cur.next:
            cur = cur.next
        cur.next = Node(name, self.timestamp)
        self.timestamp += 1

    def dequeueAny(self):
        if not self.dog.next:
            target = self.cat.next
            self.cat.next = target.next
       
        elif not self.cat.next:
            target = self.dog.next
            self.dog.next = target.next
        
        elif self.dog.next.timestamp < self.cat.next.timestamp:
            target = self.dog.next
            self.dog.next = target.next  # remove from list
        else:
            target = self.cat.next
            self.cat.next = target.next
        return target.name

    def dequeueDog(self):
        target = self.dog.next
        self.dog.next = target.next
        return target.name

    def dequeueCat(self):
        target = self.cat.next
        self.cat.next = target.next
        return target.name


