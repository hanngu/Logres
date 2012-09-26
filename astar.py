
import heapq
import itertools

fraction = 0.5

class Node:

	def __init__(self, parent):
		self.parent = parent
		self.numbers = ['1','2','3','4','5','6','7','8','9']
		self.neighbours = []
		self.length = 0
		self.parent = None 

		if parent != None:
			self.length = parent.length + 1
		else:
			self.length = 0

	def __lt__(self, other): #Less than. 
		return self.h() < other.h()

	def f(self):
		return g() + h()

	def h(self):
		return 1

	def g(self):
		return length

	def __repr__(self):
		return ''.join(self.numbers)

def isCorrectFraction(node):
	number = ''.join(node.numbers)
	numerator = float(number[0:4])
	denominator = float(number[4:9])
	thisFraction = numerator/denominator

	if abs(thisFraction - fraction) < 0.001:
		return True
	else:
		return False


def findPath(startnode, isSolution):
	print 'er i findPath'
	visitedNodes = []
	toVisit = []
	currentNode = startnode

	while True:
		visitedNodes.append(currentNode)
		for node in currentNode.neighbours:
			if node not in visitedNodes:
				heapq.heappush(toVisit, node) #pushing the node in to to visit in correct place 		
		if isSolution(currentNode):
			path = []
			while True:
				path.append(currentNode) #appends the current node to the path-list. 
				currentNode = currentNode.parent #changes currentNode to the parent

				if currentNode == None: #the path is complete
					return path

		elif len(toVisit) == 0:
			print 'no solution exist'
			return []

		currentNode = heapq.heappop(toVisit)

def generateTree():
	print 'er i generateTree-'
	startnode = Node(None)
	for permutation in itertools.permutations(startnode.numbers):
		node = Node(startnode)
		startnode.neighbours.append(node)
		node.numbers = permutation

	

	return startnode

	
print findPath(generateTree(), isCorrectFraction)

		

