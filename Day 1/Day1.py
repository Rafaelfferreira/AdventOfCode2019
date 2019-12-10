import math

data = open('input.txt', 'r').read().split('\n')
fuelCounterUpper = 0

for item in data[:-1]:
	fuelRequirement = math.floor(int(item)/3) - 2
	fuelCounterUpper += fuelRequirement
	
	while fuelRequirement > 0:
		fuelRequirement = math.floor(int(fuelRequirement)/3) - 2
		if fuelRequirement > 0:
			fuelCounterUpper += fuelRequirement


print(fuelCounterUpper)