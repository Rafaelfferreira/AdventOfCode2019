# range: 245182-790572
def part1():
	startingRange = 245182
	closingRange = 790572
	possibleCombinations = 0

	for number in range(startingRange,closingRange+1): #scanning through the number
		splitNumber = list(str(number))
		splitNumber = list(map(int, splitNumber))

		smallerNumber = splitNumber[0]
		lastDigit = None
		increasing = True
		repeating = False

		for digit in splitNumber:
			#making sure that the numbers never decrease
			if digit < smallerNumber:
				increasing = False
			elif digit > smallerNumber:
				smallerNumber = digit

			if lastDigit != None:
				if digit == lastDigit:
					repeating = True
				else:
					lastDigit = digit
			else:
				lastDigit = digit

		if (increasing == True) and (repeating == True):
			possibleCombinations += 1

	print('Possible Combinations: ', possibleCombinations)


# Main
part1()