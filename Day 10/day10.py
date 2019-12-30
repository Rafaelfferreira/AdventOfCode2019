import random
import copy
import math

# reading the input
data = open('input.txt', 'r').read().split('\n')

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
def part2():
	# basePosition = (11,13)
	basePosition = (11,13) # para o input teste. x = 3 e y = 8

	# creating the list of asteroids in each quarter and adding them to the laser map in the order they will be searched.
	q2 = []
	q4 = []
	q3 = []
	q1 = []
	laserMap = [q2, q4, q3, q1]

	# maps the asteroids to each quarter
	for currentAsteroid in asteroids:
		currentQuarter = None
		currentRatio = None
		currentDistance = None

		# mapping in what quarter is the current asteroid
		# obs: If the asteroid is in one of the dividing lines it is mapped as if it was -1 in the coordinate that coincides with the line 
		if currentAsteroid[0] < basePosition[0]: # Q1 or Q3
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
				currentRatio = float('-inf') # "right"
			else:
				currentRatio = float('inf') # "left"
		elif currentAsteroid[0] - basePosition[0] == 0: # if the asteroid is in the x axis of the base
			if currentAsteroid[1] - basePosition[1] > 0:
				currentRatio = float('-inf') # "below"
			else:
				currentRatio = float('inf') # "above"
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

	# sorting the laser map by ratios and euclidean distance
	laserMap[0] = sorted(laserMap[0], key=lambda x: (x[0],-x[1]), reverse=True)
	laserMap[1] = sorted(laserMap[1], key=lambda x: (x[0],-x[1]), reverse=True)
	laserMap[2] = sorted(laserMap[2], key=lambda x: (x[0],-x[1]), reverse=True)
	laserMap[3] = sorted(laserMap[3], key=lambda x: (x[0],-x[1]), reverse=True)

	finalLaserMap = laserMap[0] + laserMap[1] + laserMap[2] + laserMap[3]
	
	# eliminating each asteroid and keeping track of the order
	currentAsteroidIndex = 1
	asteroid200 = None

	while len(finalLaserMap) > 0:
		asteroidsToRemove = []
		lastRatio = None

		for asteroid in finalLaserMap:
			if asteroid[0] != lastRatio:
				# print(currentAsteroidIndex, " - ", asteroid)
				asteroidsToRemove.append(asteroid)
				
				if currentAsteroidIndex == 200:
					asteroid200 = asteroid
				
				currentAsteroidIndex += 1
			lastRatio = asteroid[0]

		for item in asteroidsToRemove:
			finalLaserMap.remove(item)

	print("200th Asteroid: ", asteroid200[2])
	print("Part 2 asnwer: ", (asteroid200[2][0] * 100) + asteroid200[2][1])
# main program
# part1()
part2()

