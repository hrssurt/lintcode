from stack import Stack

def sort_with_two_stacks(stack_a, stack_b):
	# we let stack_b to be always sorted
	max_item = stack_a.peek()
	sorted_size = 0
	while True:
		while stack_a.size():
			top_item = stack_a.pop()
			max_item = max(top_item, max_item)
			stack_b.push(top_item)

		while stack_b.size() != sorted_size:
			top_item = stack_b.pop()
			if top_item is not max_item:
				stack_a.push(top_item)

		# first sorted item into the stack
		stack_b.push(max_item)
		sorted_size += 1
		max_item = stack_a.peek()
		if not stack_a.size():
			break



if __name__ == '__main__':
	stack_a = Stack([2,5,6,8,7,4,11,10,22,18])
	stack_b = Stack()
	sort_with_two_stacks(stack_a, stack_b)
	print(stack_b.stack)
