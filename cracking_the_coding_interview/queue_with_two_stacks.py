from stack import Stack
class QueueS(object):
	"""docstring for QueueS"""
	def __init__(self):
		self.left = Stack()
		self.right = Stack()

	def push(self, item):
		self.left.push(item)

	def pop(self):
		while self.left.size() > 1:
			top = self.left.pop()
			self.right.push(top)

		rtn_item = self.left.pop()
		# right now the left is empty
		while self.right.size():
			top = self.right.pop()
			self.left.push(top)
		return rtn_item

if __name__ == '__main__':
	q = QueueS()
	q.push(1)
	q.push(2)
	q.push(3)
	q.push(4)
	assert(1 == q.pop())
	assert(2 == q.pop())
	assert(3 == q.pop())
	q.push(5)
	assert(4 == q.pop())
	assert(5 == q.pop())

		