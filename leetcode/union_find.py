class UnionFind(object):
 	def __init__(self, lst_of_elements):
 		self.d = {}
 		for e in lst_of_elements:
 			d[e] = e


 	def find(self, target):
 		x = target
 		while self.d[x] != x:
 			x = self.d[x]

 		# compress the path
 		while target != x:
 			temp = self.d[target]
 			self.d[target] = x
 			target = temp

 		return x

 	def join(self, x, y):
 		x_parent, y_parent = self.find(x), self.find(y)
 		self.d[y] = x_parent








