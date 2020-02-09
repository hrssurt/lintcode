# doing add without using any arithmatic operaters like +, - , * , /

def add(x, y):
	if x == 0:
		return y
	carry = (x & y) << 1 
	rest =  x ^ y
	return add(carry, rest)


if __name__ == '__main__':
	assert(5 == add(2,3))
	assert(8 == add(add(2,3),3))
	assert(13 == add(add(2,3), add(5,3)))