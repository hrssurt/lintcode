class soln(object):
	def __init__(self):
		self.time = 0	# global time tracker

	def process_edges(self, edges, neighbours):
		for p, c in edges:
			if p in neighbours:
				neighbours[p].append(c)
			else:
				neighbours[p] = [c]

			if c in neighbours:
				neighbours[c].append(p)
			else:
				neighbours[c] = [p]


	def find_cut_vertices(self, numNodes, numEdges, edges):
		visited = set()   # track the visited nodes
		cv = set()        # track the returned cut points
		start_point = 0	  # the point we use to do our dfs traversal

		# four more dictinaries
		parent = {}		  # given a node, return its parent
		low_time = {}     # given a node, track its low time
		visited_time = {} # given a node, the time it is first visited
		neighbours = {}   # given a node, track its neighbours

		# first, transform input and build neighbours
		self.process_edges(edges, neighbours)

		# initialize parent
		for i in range(numNodes):
			parent[i] = None

		# doing dfs traversal from start_point
		self.dfs(start_point, visited, cv, visited_time, low_time, parent, neighbours)
		return sorted(list(cv))

	def dfs(self, cur_node, visited, cv, visited_time, low_time, parent, neighbours):
		visited.add(cur_node)
		visited_time[cur_node] = self.time
		low_time[cur_node] = self.time
		self.time += 1
		child_count = 0
		is_cv_point = False

		for neighbour in neighbours[cur_node]:
			if neighbour == parent[cur_node]:	# the neighbour is the parent of the current node,
												# just ignore
				continue

			# check if neightbour is visited
			if neighbour not in visited:
				parent[neighbour] = cur_node
				child_count += 1
				self.dfs(neighbour, visited, cv, visited_time, low_time, parent, neighbours)	# recursion to 

				if visited_time[cur_node] <= low_time[neighbour]:
					is_cv_point = True

				else:
					# we need to do lowtime[cur_node] = min(lowtime[cur_node], lowtime[n])
					low_time[cur_node] = min(low_time[cur_node], low_time[neighbour])
			else:
				# if it is already visited, lets see if we can update the low time
				low_time[cur_node] = min(low_time[cur_node], visited_time[neighbour])


		
		# after traversing all the neighbours, we can tell if the node is cv or not
		if child_count >= 2 and parent[cur_node] is None:        # it is a starting node and have more than one child
			cv.add(cur_node)


		elif is_cv_point and parent[cur_node] is not None:		 # the flag is set to true and it is not a root node
			cv.add(cur_node)

def brute_force_soln(numNodes, edges):
	# each time we remove a node
	# if removing this node results in a diconnected graph,
	# add this to cv set
	cv = set()
	for cur_node in range(numNodes):
		new_edges = [lst for lst in edges if cur_node not in lst]	# remove all edges that contain this node
		neighbours = {}
		for p,c in new_edges:
			if p in neighbours:
				neighbours[p].add(c)
			else:
				neighbours[p] = set([c])

			if c in neighbours:
				neighbours[c].add(p)
			else:
				neighbours[c] = set([p])
			

		if not edges:		# there is no remaining, this one is a cv
			cv.add(cur_node)
		else:
			# using bfs
			starting_node = new_edges[0][0]
			q = [starting_node]
			visited = set([starting_node])
			while q:
				top = q.pop(0)
				for n in neighbours[top]:
					if n not in visited:
						q.append(n)
						visited.add(n)

			if len(visited) < numNodes - 1:
				cv.add(cur_node)
	return sorted(list(cv))



if __name__ == '__main__':
	obj = soln()
	# some test cases
	numNodes = 7
	numEdges = 7 
	edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
	print(obj.find_cut_vertices(numNodes, numEdges, edges))
	print(brute_force_soln(numNodes, edges))

	numEdges = 5
	numNodes = 5
	obj.time = 0
	edges = [(1, 0), (0, 2), (2, 1), (0, 3), (3, 4)] 
	print(obj.find_cut_vertices(numNodes, numEdges, edges))
	print(brute_force_soln(numNodes, edges))


	numNodes = 4
	numEdges = 3
	obj.time = 0
	edges = [[0,1], [1,2], [2,3]]
	print(obj.find_cut_vertices(numNodes, numEdges, edges))
	print(brute_force_soln(numNodes, edges))


	numNodes = 7
	numEdges = 7
	obj.time = 0
	edges = [[0,1], [1,2], [2,0], [1,3], [1,4], [1,6], [3,5], [4,5]]
	print(obj.find_cut_vertices(numNodes, numEdges, edges))
	print(brute_force_soln(numNodes, edges))
	
	










