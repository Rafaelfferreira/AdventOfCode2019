#Getting the input
preInput = open('input.txt', 'r').read().split('\n')
wire1 = preInput[0].split(',')
wire2 = preInput[1].split(',')

#test variables
#wire1 = ['R8','U5','L5','D3']
#wire2 = ['U7','R6','D4','L4']

# wire1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
# wire2 = ['U62','R66','U55','R34','D71','R55','D58','R83']

# wire1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
# wire2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __hash__(self):
		return hash((self.x, self.y))

	def __eq__(self, other):
		return (self.x == other.x) and (self.y == other.y)

def calculateWire1Points(pointsWire1):
	currentPosition = Point(0,0)

	for command in wire1:
		direction = command[0]
		steps = int(command[1:])
		#print('direction: ', direction, ' steps: ', steps)
		for movement in range(0, steps):
			if direction == 'L':
				newPoint = Point(currentPosition.x-1, currentPosition.y)
			elif direction == 'R':
				newPoint = Point(currentPosition.x+1, currentPosition.y)
			elif direction == 'U':
				newPoint = Point(currentPosition.x, currentPosition.y+1)
			elif direction == 'D':
				newPoint = Point(currentPosition.x, currentPosition.y-1)

			#print(newPoint.x, newPoint.y)
			pointsWire1.add(newPoint)
			currentPosition = newPoint

def calculateManhattanDistance(point):
	#|x1 - x2| + |y1 - y2|
	return abs(point.x) + abs(point.y)


#check every point on the second wire and, if they intersect with one on the first wire checks if their manhattan distance is lower than the currently lower one
def findClosestIntersection(pointsWire1): 
	smallerManhattanDistance = float('inf')
	currentPosition = Point(0,0)

	for command in wire2:
		direction = command[0]
		steps = int(command[1:])
		#print('direction: ', direction, ' steps: ', steps)
		for movement in range(0, steps):
			if direction == 'L':
				newPoint = Point(currentPosition.x-1, currentPosition.y)
			elif direction == 'R':
				newPoint = Point(currentPosition.x+1, currentPosition.y)
			elif direction == 'U':
				newPoint = Point(currentPosition.x, currentPosition.y+1)
			elif direction == 'D':
				newPoint = Point(currentPosition.x, currentPosition.y-1)

			if newPoint in pointsWire1:
				currentManhattanDistance = calculateManhattanDistance(newPoint)
				if currentManhattanDistance < smallerManhattanDistance:
					smallerManhattanDistance = currentManhattanDistance

			currentPosition = newPoint

	return smallerManhattanDistance


#Part 1
pointsWire1 = set()
calculateWire1Points(pointsWire1)
print(findClosestIntersection(pointsWire1))
