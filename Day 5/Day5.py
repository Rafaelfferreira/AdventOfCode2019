#importing libraries
import copy

#reading the input
data = open('input.txt', 'r').read().split(',')
data = list(map(int, data))

def opcodeComputer(input):
	cursorPosition = 0 #starting position of the cursor
	instructionJump = 4

	while data[cursorPosition] != 99:
		# separating each component of the opcode
		digits = getIndividualDigits(data[cursorPosition])
		opcode = int(str(digits[3]) + str(digits[4]))
		parameter1Mode = digits[2]
		parameter2Mode = digits[1]
		parameter3Mode = digits[0]
		#print(data[225])
		#print(cursorPosition, ': ', opcode, ' - Digits: ', digits)

		if opcode == 1:
			addInstruction(cursorPosition, parameter1Mode, parameter2Mode, parameter3Mode)
			#data[data[cursorPosition+3]] = (data[data[cursorPosition+1]] + data[data[cursorPosition+2]])
			instructionJump = 4
		elif opcode == 2:
			multiplyInstruction(cursorPosition, parameter1Mode, parameter2Mode, parameter3Mode)
			#data[data[cursorPosition+3]] = (data[data[cursorPosition+1]] * data[data[cursorPosition+2]])
			instructionJump = 4
		elif opcode == 3:
			saveInstruction(cursorPosition, parameter1Mode, input)
			#data[data[cursorPosition+1]] = input.pop(0)
			instructionJump = 2
		elif opcode == 4:
			retrieveInstruction(cursorPosition, parameter1Mode)
			#print(data[data[cursorPosition+1]])
			instructionJump = 2
		
		if cursorPosition+instructionJump > len(data): # MODIFICAR ISSO PARA O TAMANHO DE AUMENTO DO CURSOR SER VARIAVEL
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

def addInstruction(cursorPosition, parameter1Mode, parameter2Mode, parameter3Mode):
	#first parameter
	if parameter1Mode == 1:
		sum = data[cursorPosition+1]
	else:
		sum = data[data[cursorPosition+1]]

	#second parameter
	if parameter2Mode == 1:
		sum += data[cursorPosition+2]
	else:
		sum += data[data[cursorPosition+2]]

	#third parameter
	if parameter3Mode == 1:
		data[cursorPosition+3] = sum
	else:
		data[data[cursorPosition+3]] = sum

def multiplyInstruction(cursorPosition, parameter1Mode, parameter2Mode, parameter3Mode):
	#first parameter
	if parameter1Mode == 1:
		total = data[cursorPosition+1]
	else:
		total = data[data[cursorPosition+1]]

	#second parameter
	if parameter2Mode == 1:
		total = total * data[cursorPosition+2]
	else:
		total = total * data[data[cursorPosition+2]]

	#third parameter
	if parameter3Mode == 1:
		data[cursorPosition+3] = total
	else:
		data[data[cursorPosition+3]] = total

def saveInstruction(cursorPosition, parameter1Mode, input):
	if parameter1Mode == 1:
		data[cursorPosition+1] = input.pop(0)
	else:
		data[data[cursorPosition+1]] = input.pop(0)

def retrieveInstruction(cursorPosition, parameter1Mode):
	if parameter1Mode == 1:
		print(data[cursorPosition+1])
	else:
		print(data[data[cursorPosition+1]])



# main program
opcodeComputer([1])

#testes:
# digits = getIndividualDigits(1012)
# opcode = int(str(digits[3]) + str(digits[4]))
# print(opcode)



