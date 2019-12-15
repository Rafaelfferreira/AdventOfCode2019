# reading the input
data = open('input.txt', 'r').read().split('\n')

#setting up the input as a list of tuples
mapData = [] #raw data with tuples representing an object and his direct satellite
galaxyGraph = {}

for entry in data:
	orbitData = entry.split(')')
	mapData.append(orbitData)

# defining the structure of every object in space
class spaceObjects:
	def __init__(self, name, directOrbit):
		self.name = name
		self.directOrbit = directOrbit #another space Object
		self.satellites = [] #a set of space objects

		def __hash__(self):
			return hash((self.name))


#criando o Universal Center of Mass (COM)
COM = spaceObjects('COM', None)
galaxyGraph[COM.name] = COM


# populating the galaxy graph
for entry in mapData: #E each entry is a tuple with an object and its satelite
	if entry[0] not in galaxyGraph:
		galaxyGraph[entry[0]] = spaceObjects(entry[0], None)

	if entry[1] not in galaxyGraph:
		galaxyGraph[entry[1]] = spaceObjects(entry[1], entry[0])
	else: 
		galaxyGraph[entry[1]].directOrbit = entry[0]

	galaxyGraph[entry[0]].satellites.append(entry[1])


def calculateOrbits(object, totalOrbits, height):
	if len(object.satellites) == 0:
		return height
	else:
		tempOrbits = 0
		for satellite in object.satellites:
			tempOrbits += calculateOrbits(galaxyGraph[satellite], totalOrbits, height+1)
		totalOrbits += height + tempOrbits

	return totalOrbits


# main 
totalOrbits = 0
height = 0
totalOrbits = calculateOrbits(galaxyGraph['COM'], totalOrbits, height)
print(totalOrbits)