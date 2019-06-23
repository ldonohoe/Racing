from collections import defaultdict

class Node():

	def __init__(self, tile, rot):
		self.id = 0
		self.tile = tile
		self.rot = rot
		self.connected = []


	def addEdge(self, node):
		self.connected.append(node)
		node.addEdge(self)



def findNode(start, end):
	visited = []
	queue = []
	path = []
	queue.append(start)
	visited.append(start)
	while queue:
		s = queue.pop(0)
		for node in s.connected:
			if node.id = end.id:
				return path
			elif node in visited:
				pass
			else:
				queue.append(node)