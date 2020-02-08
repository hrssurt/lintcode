# swap two numbers without creating a temperaory variable

def swap(a, b):
	# in python, we can directy do a, b = b, a
	# but that is language special. we will use the more general method that can be used in all languages

	a = a + b
	b = a - b  # now b has a's original value
	a = a - b  # now a has b's original value

	return a, b

if __name__ == '__main__':
	assert((1,2) == swap(2,1))
	assert((1,5) == swap(5,1))