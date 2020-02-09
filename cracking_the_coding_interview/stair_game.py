def stair_game(n):
	a,b,c = 1,2,3
	for _ in range(n-1):
		a,b,c = b,c,a+b+c
	return a

if __name__ == '__main__':
	assert(stair_game(1) == 1)
	assert(stair_game(2) == 2)
	assert(stair_game(3) == 3)
	assert(stair_game(4) == 6)