import random
import copy

# reading the input
data = open('input.txt', 'r').read().split('\n')

asteroids = set()

# mapping which points contain asteroids
for y in range(0,len(data)):
	for x in range(0, len(data[y])):
		if data[y][x] == '#':
			asteroids.add((x,y))

# avaliating the asteroid where you can see the most other asteroids
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



