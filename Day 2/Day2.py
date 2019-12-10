#importing libraries
import copy

#reading the input
data = open('input.txt', 'r').read().split(',')
data = list(map(int, data))

#Part 1
#doing the replacements specified 
data[1] = 12
data[2] = 2

def calculateOutputPart1():
	cursorPosition = 0 #starting position of the cursor
	while data[cursorPosition] != 99:
		if data[cursorPosition] == 1:
			data[data[cursorPosition+3]] = (data[data[cursorPosition+1]] + data[data[cursorPosition+2]])
		elif data[cursorPosition] == 2:
			data[data[cursorPosition+3]] = (data[data[cursorPosition+1]] * data[data[cursorPosition+2]])
		
		if cursorPosition+4 > len(data):
			break
		else:
			cursorPosition += 4
	
	print(data[0])


def calculateOutputPart2(noun, verb):
	tempData = copy.deepcopy(data)
	tempData[1] = noun
	tempData[2] = verb
	instructionPointer = 0 #starting position of the cursor

	while tempData[instructionPointer] != 99:
		if tempData[instructionPointer] == 1:
			tempData[tempData[instructionPointer+3]] = (tempData[tempData[instructionPointer+1]] + tempData[tempData[instructionPointer+2]])
		elif tempData[instructionPointer] == 2:
			tempData[tempData[instructionPointer+3]] = (tempData[tempData[instructionPointer+1]] * tempData[tempData[instructionPointer+2]])
		
		if instructionPointer+4 > len(tempData):
			break
		else:
			instructionPointer += 4

	return tempData[0]

#Part 2
for noun in range(0,100):
	for verb in range(0,100):
		output = calculateOutputPart2(noun,verb)
		if output == 19690720:
			print('noun: ', noun)
			print('verb: ', verb)
			print('answer: ', (100 * noun) + verb)

