#importing libraries
import copy

#reading the input
data = open('input.txt', 'r').read().split(',')
data = list(map(int, data))
data.extend([0] * max(data))

def opcodeComputer(input):
	cursorPosition = 0 #starting position of the cursor
	relativeBase = 0
	instructionJump = 4

	while data[cursorPosition] != 99:
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
			retrieveInstruction(valueParameter1)
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
	# print("Vai imprimir da posicao: ", valueParameter1)
	print(data[valueParameter1])

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
	# print("Mudanca da base relativa: ", data[valueParameter1])
	# input()
	return data[valueParameter1]


# main program
opcodeComputer([2])


