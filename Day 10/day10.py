import random
import copy
import math

# reading the input
data = open('inputTeste.txt', 'r').read().split('\n')

asteroids = set()

# mapping which points contain asteroids
for y in range(0,len(data)):
	for x in range(0, len(data[y])):
		if data[y][x] == '#':
			asteroids.add((x,y))


# Explanation of the part 1 algorithm:
# The idea is that the line between each two asteroids has a ratio of dx and dy.
# What we do is find the ratio of each line dividing dx/dy. If 2 asteroids have the same ratio starting from the same asteroid then one of them blocks the other.
# The way to find out how many different asteroids are observable is to find out how many different ratios you can get with the same starting asteroids
# Obs: If you consider the current asteroid as the center of a quadrant, the ratios in the quarters q1,q3 and q2,q4 are the same, so we save the quarter as well as the ratio
# so that we can separate ratios with the same value in different quarters.

# PART 1
# avaliating the asteroid where you can see the most other asteroids
def part1():	
	optimalAsteroid = random.sample(asteroids, 1)
	optimalAsteroidVisibleAsteroids = set()

	for currentAsteroid in asteroids: # going through each asteroid
		visibleAsteroidRatios = set()
		possibleAsteroids = copy.deepcopy(asteroids)
		possibleAsteroids.remove(currentAsteroid)

		for otherAsteroid in possibleAsteroids: # Checking if the other asteroids are visible from CurrentAsteroid

			if otherAsteroid[1] - currentAsteroid[1] == 0: # if the asteroid is in the y axis of the base

				if otherAsteroid[0] - currentAsteroid[0] > 0:
					visibleAsteroidRatios.add("right")
				else:
					visibleAsteroidRatios.add("left")
			else:
				currentRatio = (otherAsteroid[0] - currentAsteroid[0])/(otherAsteroid[1] - currentAsteroid[1])
				currentRatio = round(currentRatio, 3)


				# This part is important because points in the quarter 1-3 and 2-4  have the same ratio, but we need to differentiate them somehow on the set
				if otherAsteroid[0] < currentAsteroid[0]: # Q1 or Q3
					if otherAsteroid[1] < currentAsteroid[1]: 
						visibleAsteroidRatios.add((currentRatio, "q3"))
					else:
						visibleAsteroidRatios.add((currentRatio, "q1"))
				else:
					if otherAsteroid[1] < currentAsteroid[1]: # Q2 or Q4
						visibleAsteroidRatios.add((currentRatio, "q4"))
					else:
						visibleAsteroidRatios.add((currentRatio, "q2"))

		if len(visibleAsteroidRatios) > len(optimalAsteroidVisibleAsteroids):
			optimalAsteroid = currentAsteroid
			optimalAsteroidVisibleAsteroids = visibleAsteroidRatios

	print("Optimal Asteroid: ", optimalAsteroid)
	print("Observable asteroids from optimal point: ", len(optimalAsteroidVisibleAsteroids))


# PART 2
# basePosition = (11,13)
basePosition = (8,3) # para o input teste. x = 3 e y = 8

# creating the list of asteroids in each quarter and adding them to the laser map in the order they will be searched.
q2 = []
q4 = []
q3 = []
q1 = []
laserMap = [q2, q4, q3, q1]

for currentAsteroid in asteroids:
	currentQuarter = None
	currentRatio = None
	currentDistance = None

	# mapping in what quarter is the current asteroid
	# obs: If the asteroid is in one of the dividing lines it is mapped as if it was -1 in the coordinate that coincides with the line 
	if currentAsteroid[0] <= basePosition[0]: # Q1 or Q3
		if currentAsteroid[1] > basePosition[1]: 
			currentQuarter = 'q3'
		else:
			currentQuarter = 'q1'
	else:
		if currentAsteroid[1] > basePosition[1]: # Q2 or Q4
			currentQuarter = 'q4'
		else:
			currentQuarter = 'q2'

	# calculating the ratio
	if currentAsteroid[1] - basePosition[1] == 0: # if the asteroid is in the y axis of the base
		if currentAsteroid[0] - basePosition[0] > 0:
			currentRatio = "right"
		else:
			currentRatio = "left"
	else:
		currentRatio = (currentAsteroid[0] - basePosition[0])/(currentAsteroid[1] - basePosition[1])
		currentRatio = round(currentRatio, 3)

	# calculating the euclidean distance
	currentDistance = math.sqrt(pow(currentAsteroid[0] - basePosition[0], 2) + pow(currentAsteroid[1] - basePosition[1], 2))
	currentDistance = round(currentDistance, 3)

	# print("Teste: ", (currentRatio, currentDistance, currentAsteroid))

	# saving the necessary information in the correct quarter list
	if currentQuarter == 'q1':
		q1.append((currentRatio, currentDistance, currentAsteroid))
	elif currentQuarter == 'q2':
		q2.append((currentRatio, currentDistance, currentAsteroid))
	elif currentQuarter == 'q3':
		q3.append((currentRatio, currentDistance, currentAsteroid))
	elif currentQuarter == 'q4':
		q4.append((currentRatio, currentDistance, currentAsteroid))



# main program
# part1()


# test prints
# data[3][8] = 'R'
# for line in data:
# 	print(line)
# print(data[3][8])
# print(asteroids)

#um exemplo de sort using lambda funciont
# print(laserMap)
print("Q2: ")
print(laserMap[0])
print("Quantidade: ", len(laserMap[0]))

print("\nQ4: ")
print(laserMap[1])
print("Quantidade: ", len(laserMap[1]))

print("\nQ3: ")
print(laserMap[2])
print("Quantidade: ", len(laserMap[2]))

print("\nQ1: ")
print(laserMap[3])
print("Quantidade: ", len(laserMap[3]))

for i in range(0, len(laserMap)):
# 	for asteroid in laserMap[i]:
# 		if asteroid[0] == None:
# 			print("ACHOU")
	print(len(laserMap[i]))
# print(pow(3,2))
# print(sorted([('abc', 121),('abc', 231),('abc', 148), ('abc',221)], key=lambda x: x[1]))


