#importing libraries
import copy

#reading the input
data = open('input.txt', 'r').read().split(',')
data = list(map(int, data))
data.extend([0] * 100000)

# ------------------------------------------------------------------------------------------------------
# OPCode Computer Definition and auxiliary functions
# ------------------------------------------------------------------------------------------------------

def paintingRobot(input):
	output = []
	cursorPosition = 0 #starting position of the cursor
	relativeBase = 0
	instructionJump = 4
	facingDirection = "up"
	currentPosition = [0,0]
	paintedPanels = set()
	paintedColors = {}

	while data[cursorPosition] != 99:
		while len(output) < 2 and data[cursorPosition] != 99:
			# separating each component of the opcode
			digits = getIndividualDigits(data[cursorPosition])
			opcode = int(str(digits[3]) + str(digits[4]))
			parameter1Mode = digits[2]
			parameter2Mode = digits[1]
			parameter3Mode = digits[0]
			instructionJump = 0
			# print(cursorPosition, ': ', opcode, ' - Digits: ', digits)

			# parameter 1
			if parameter1Mode == 0:
				valueParameter1 = data[cursorPosition+1]
			elif parameter1Mode == 1:
				valueParameter1 = cursorPosition+1
			elif parameter1Mode == 2:
				valueParameter1 = data[cursorPosition+1] + relativeBase
				

			# parameter 2
			if parameter2Mode == 0:
				valueParameter2 = data[cursorPosition+2]
			elif parameter2Mode == 1:
				valueParameter2 = cursorPosition+2
			elif parameter2Mode == 2:
				valueParameter2 = data[cursorPosition+2] + relativeBase

			# parameter 3
			if parameter3Mode == 0:
				valueParameter3 = data[cursorPosition+3]
			elif parameter3Mode == 1:
				valueParameter3 = cursorPosition+3
			elif parameter3Mode == 2:
				valueParameter3 = data[cursorPosition+3] + relativeBase


			if opcode == 1:
				addInstruction(valueParameter1, valueParameter2, valueParameter3)
				instructionJump = 4
			elif opcode == 2:
				multiplyInstruction(valueParameter1, valueParameter2, valueParameter3)
				instructionJump = 4
			elif opcode == 3:
				saveInstruction(valueParameter1, input)
				instructionJump = 2
			elif opcode == 4:
				output.append(retrieveInstruction(valueParameter1))
				instructionJump = 2
			elif opcode == 5:
				cursorPosition = jumpIfTrue(cursorPosition, valueParameter1, valueParameter2)
			elif opcode == 6:
				cursorPosition = jumpIfFalse(cursorPosition, valueParameter1, valueParameter2)
			elif opcode == 7:
				lessThen(valueParameter1, valueParameter2, valueParameter3)
				instructionJump = 4
			elif opcode == 8:
				equals(valueParameter1, valueParameter2, valueParameter3)
				instructionJump = 4
			elif opcode == 9:
				relativeBase += adjustRelativeBase(valueParameter1)
				instructionJump = 2



			# input()
			if cursorPosition+instructionJump > len(data):
				break
			else:
				cursorPosition += instructionJump

		if data[cursorPosition] != 99:
			# print("Painel atual: ", currentPosition, " - cor a ser pintada: ", output[0])

			# saving data about the current panel and cleaning the output var
			currentPanel = (currentPosition[0], currentPosition[1])
			paintedPanels.add(currentPanel) # saving the position of the current panel, used to count how many panels were painted
			paintedColors[currentPanel] = output[0] # saving the color the current panel
			facingDirection = turnRobot(facingDirection, output[1])
			output = []

			# moving the robot and updating the input
			if facingDirection == "up":
				currentPosition[1] += 1
			elif facingDirection == "left":
				currentPosition[0] -= 1
			elif facingDirection == "right":
				currentPosition[0] += 1
			else: # "down"
				currentPosition[1] -= 1


			currentPanel = (currentPosition[0], currentPosition[1])
			# print("Andou na direcao: ", facingDirection, " - E esta na posicao: ", currentPanel, "\n")
			if (currentPanel) in paintedColors:
				input.append(paintedColors[currentPanel])
			else:
				input.append(0)
			# PROCESSING

	print(len(paintedPanels))

# Used to get the opcodes in the default 5 digit array (where the numbers ommited at the front are 0)
def getIndividualDigits(number):
	digits = [0,0,0,0,0]
	number = [int(digit) for digit in str(number)] #separating the number into a list of digits

	# mapping the numbers to fit the always 5 digit array
	lastIndexDigits = len(digits)-1
	lastIndexOPCode = len(number)-1

	while lastIndexOPCode >= 0:
		digits[lastIndexDigits] = number[lastIndexOPCode]
		lastIndexDigits -= 1
		lastIndexOPCode -= 1

	return digits

def addInstruction(valueParameter1, valueParameter2, valueParameter3):
	sum = data[valueParameter1] + data[valueParameter2]
	data[valueParameter3] = sum

def multiplyInstruction(valueParameter1, valueParameter2, valueParameter3):
	total = data[valueParameter1] * data[valueParameter2]
	data[valueParameter3] = total

def saveInstruction(valueParameter1, input):
	data[valueParameter1] = input.pop(0)

def retrieveInstruction(valueParameter1):
	return data[valueParameter1]

def jumpIfTrue(cursorPosition, valueParameter1, valueParameter2):
	if data[valueParameter1] != 0:
		cursorPosition = data[valueParameter2]
	else:
		if cursorPosition+3 < len(data):
			cursorPosition += 3

	return cursorPosition

def jumpIfFalse(cursorPosition, valueParameter1, valueParameter2):
	if data[valueParameter1] == 0:
		cursorPosition = data[valueParameter2]
	else:
		if cursorPosition+3 < len(data):
			cursorPosition += 3

	return cursorPosition

def lessThen(valueParameter1, valueParameter2, valueParameter3):
	if data[valueParameter1] < data[valueParameter2]:
		data[valueParameter3] = 1
	else:
		data[valueParameter3] = 0

def equals(valueParameter1, valueParameter2, valueParameter3):
	if data[valueParameter1] == data[valueParameter2]:
		data[valueParameter3] = 1
	else:
		data[valueParameter3] = 0

def adjustRelativeBase(valueParameter1):
	return data[valueParameter1]

def turnRobot(facingDirection, turning):
	if facingDirection == "up":
		if turning == 0:
			return "left"
		else:
			return "right"
	elif facingDirection == "left":
		if turning == 0:
			return "down"
		else:
			return "up"
	elif facingDirection == "right":
		if turning == 0:
			return "up"
		else:
			return "down"
	elif facingDirection == "down":
		if turning == 0:
			return "right"
		else:
			return "left"

# ------------------------------------------------------------------------------------------------------

# def paintingRobot:
# 	def __init__(self):
# 		self.computer = opcodeComputer()
# 		self.direction = "up"


# main program
paintingRobot([0])
