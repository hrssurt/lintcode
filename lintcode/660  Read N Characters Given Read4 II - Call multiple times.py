"""***************************  TITLE  ****************************"""
"""660  Read N Characters Given Read4 II - Call multiple times.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
The API: int read4(char *buf) reads 4 characters at a time from a file.
"""



"""***************************  EXAMPLES  ****************************"""
"""
int read4(char *buf)
"""



"""***************************  CODE  ****************************"""
class Solution:
    def __init__(self):
        self.buffer = []
        self.read_complete = False
    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def copy(self, source, target):
        for idx, char in enumerate(source):
            target[idx] = char
    
    def read(self, buf, n):
        if not n:
            return 0
            
        # file is not empty
        size = len(self.buffer)
        while size < n and not self.read_complete:
            temp = [None for _ in range(4)]
            r = Reader.read4(temp)
            temp = [item for item in temp if item is not None]  # get rid of None
            if r < 4:
                self.read_complete = True
            self.buffer += temp
            size += r
        print(self.buffer)
        
        # now there are three cases:
        # 1. n is greater or equal to what we have
        # 2. we read more than what we need
        if n >= len(self.buffer):   # request more than needed, just give it all
            self.copy(self.buffer, buf)
            size = len(self.buffer)
            self.buffer = []
            return size
        else:
            self.copy(self.buffer[0:n], buf)
            self.buffer = self.buffer[n:]
            return n
