class Stack(object):
	"""Last in first out"""
	def __init__(self):
		self.stack = []

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		return self.stack.pop(-1)

	def size(self):
		return len(self.stack)
		

if __name__ == '__main__':
	s = Stack()
	s.push(1)
	s.push(2)
	s.push(3)
	assert(3 == s.pop())
	assert(2 == s.pop())
	s.push(4)
	assert(4 == s.pop())
	assert(1 == s.pop())