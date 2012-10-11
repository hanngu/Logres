from math import exp
import random
from copy import deepcopy

max_eggs = 30
max_k = 3
dT = 0.005

class Carton:

	def __init__(self, x, y):
		self.width = x
		self.height = y
		self.cells = []
		for i in range(x):
			row = []
			for j in range(y):
				row.append(0)
			self.cells.append(row)

	def __repr__(self): #make node printable
		ret = ""
		for row in self.cells:
			for cell in row:
				ret += str(cell)
			ret += "\n"
		return ret


	def score(self):

		ant = 0

		for row in self.cells:
			for cell in row:
				ant += cell

		return ant

	def generate_neighbor(self):

		neighbors = []

		for i in range(1, self.width*self.height):
			neighbor = Carton(self.width, self.height)
			neighbor.cells = deepcopy(self.cells)

			while True:
				x = random.randint(0, self.width - 1)
				y = random.randint(0, self.height - 1)

				if(neighbor.cells[x][y] == 0):
					neighbor.cells[x][y] = 1
					break
					

			if(neighbor.is_valid()):

				neighbors.append(neighbor)

		return neighbors





		

	def is_valid(self):

		#Checking if it's valid in rows
		for row in self.cells:
			ant = 0
			for cell in row:
				ant += cell
				if (ant > max_k):
					return False

		#Checking if it's valid in columns
		for x in range(self.height):
			ant = 0
			for y in range(self.width):
				ant += self.cells[y][x]
				if (ant > max_k):
					return False

		#Checking if it's valid diagonally
		for i in range(self.height):
			x1 = i # rows
			y1 = 0
			ant1 = 0
			x2 = 0 # columns
			y2 = i
			ant2 = 0

			for j in range(self.height-i):
				ant1 += self.cells[x1][y1]
				x1 += 1
				y1 += 1
				#print y1
				ant2 += self.cells[x2][y2]
				x2 += 1
				y2 += 1


				if (ant1 > max_k or ant2 > max_k):
					return False

		#Checking if it's valid diagonally			
		for i in range(self.height, 0, -1): # last argument is step, we need to set step manually to -1
			x1 = i# rows
			y1 = self.width
			ant1 = 0
			x2 = self.height # columns
			y2 = i
			ant2 = 0
			for j in range(self.height-i, 0):
				ant1 += self.cells[x1][y1]
				x1 -= 1
				y1 -= 1

				ant2 += self.cells[x2][y2]
				x2 -= 1
				y2 -= 1

				if (ant1 > max_k or ant2 > max_k):
					return False

		return True

def simulated_annealing(start):

	carton = start
	temp = 1.0

	if(carton.score() == max_eggs):
		return carton

	while(carton.score() < max_eggs):
		print carton
		neighbors = carton.generate_neighbor()

		max_neigh = 0
		best_neighbor = neighbors[0]
		for i in neighbors:
			current_score = i.score()
			if(current_score> max_neigh):
				max_neigh = current_score
				best_neighbor = i

		if (carton.score() == 0):
			q = 0
		else:
			q = float((max_neigh - carton.score()))/float(carton.score())


		p = min(1, exp(-q/temp))

		if(random.random() > p):
			carton = best_neighbor
		else:
			carton = random.choice(neighbors)

		temp -= dT

	return carton

start = Carton(10, 10) #setting the sizes
carton = simulated_annealing(start)
print "Solution:\n", carton

















