def soln_online(a,b,target):
    a.sort(key=lambda x: x[1])
    b.sort(key=lambda x: x[1])
    l, r = 0, len(b) - 1
    ans = []
    curDiff = float('inf')
    while l < len(a) and r >= 0:
        id1, i = a[l]
        id2, j = b[r]
        if (target - i - j == curDiff):
            ans.append([id1, id2])
        elif (i + j <= target and target - i - j < curDiff):
            ans.clear()
            ans.append([id1, id2])
            curDiff = target - i - j
        if (target > i + j):
            l += 1
        else:
            r -= 1
    return ans

def soln(a, b, target):
	if not a or not b:
		return []
	a.sort(key=lambda x: x[1])
	b.sort(key=lambda x: x[1])

	left, right = 0, len(b)-1
	result = []
	best_dif = float('inf')
	while left < len(a) and right >= 0:
		while right >= 0 and a[left][1] + b[right][1] > target:
			right -= 1

		if right < 0:
			break

		# we can be sure now that the sum is smaller or equal to target
		# find a new best 
		if target - (a[left][1] + b[right][1]) == best_dif:
			result.append([a[left][0], b[right][0]])

		elif target - (a[left][1] + b[right][1]) < best_dif:
			best_dif = target - (a[left][1] + b[right][1])
			result.clear()
			result.append([a[left][0], b[right][0]])

		left += 1

	return result

if __name__ == '__main__':
	# test case one
	a = [[1, 2], [2, 4], [3, 6]]
	b = [[1, 2]]
	target = 7

	print(soln(a,b,target))
	print(soln_online(a,b,target))
	
	# test case two
	a = [[1, 3], [2, 5], [3, 7], [4, 10]]
	b = [[1, 2], [2, 3], [3, 4], [4, 5]]
	target = 10
	print(soln(a,b,target))
	print(soln_online(a,b,target))
	
	# test case three
	a = [[1, 8], [2, 7], [3, 14]]
	b = [[1, 5], [2, 10], [3, 14]]
	target = 20

	print(soln(a,b,target))
	print(soln_online(a,b,target))

	# test case four
	a = [[1, 8], [2, 15], [3, 9]]
	b = [[1, 8], [2, 11], [3, 12]]
	target = 20
	print(soln(a,b,target))
	print(soln_online(a,b,target))
