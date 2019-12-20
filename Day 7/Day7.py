#importing libraries
import copy
import itertools

#reading the input
# data = open('inputTeste.txt', 'r').read().split(',')
# data = list(map(int, data))

class amplifier:
	def __init__(self, phaseSetting, data):
		self.cursorPosition = 0
		self.inputArray = [phaseSetting]
		self.halted = False
		self.data = data
		self.output = None

	def opcodeComputerAmp(self, input):
		self.inputArray.append(input)
		instructionJump = 4

		while self.data[self.cursorPosition] != 99:
			# separating each component of the opcode
			digits = getIndividualDigits(self.data[self.cursorPosition])
			opcode = int(str(digits[3]) + str(digits[4]))
			parameter1Mode = digits[2]
			parameter2Mode = digits[1]
			parameter3Mode = digits[0]
			instructionJump = 0

			# print(amp.cursorPosition, ': ', opcode, ' - Digits: ', digits)

			if opcode == 1:
				addInstruction(self.cursorPosition, parameter1Mode, parameter2Mode, parameter3Mode, self.data)
				instructionJump = 4
			elif opcode == 2:
				multiplyInstruction(self.cursorPosition, parameter1Mode, parameter2Mode, parameter3Mode, self.data)
				instructionJump = 4
			elif opcode == 3:
				saveInstructionLoop(self.cursorPosition, parameter1Mode, self.inputArray.pop(0), self.data)
				instructionJump = 2
			elif opcode == 4:
				self.output = retrieveInstruction(self.cursorPosition, parameter1Mode, self.data)
				instructionJump = 2
			elif opcode == 5:
				self.cursorPosition = jumpIfTrue(self.cursorPosition, parameter1Mode, parameter2Mode, self.data)
			elif opcode == 6:
				self.cursorPosition = jumpIfFalse(self.cursorPosition, parameter1Mode, parameter2Mode, self.data)
			elif opcode == 7:
				lessThen(self.cursorPosition, parameter1Mode, parameter2Mode, parameter3Mode, self.data)
				instructionJump = 4
			elif opcode == 8:
				equals(self.cursorPosition, parameter1Mode, parameter2Mode, parameter3Mode, self.data)
				instructionJump = 4

			
			if self.cursorPosition+instructionJump > len(self.data):
				break
			else:
				self.cursorPosition += instructionJump

			if opcode == 4:
				return self.output

		self.halted = True
		return self.output

def opcodeComputer(input, output):
	cursorPosition = 0 #starting position of the cursor
	instructionJump = 4

	while data[cursorPosition] != 99:
		# separating each component of the opcode
		digits = getIndividualDigits(data[cursorPosition])
		opcode = int(str(digits[3]) + str(digits[4]))
		parameter1Mode = digits[2]
		parameter2Mode = digits[1]
		parameter3Mode = digits[0]
		instructionJump = 0
		#print(cursorPosition, ': ', opcode, ' - Digits: ', digits)

		if opcode == 1:
			addInstruction(cursorPosition, parameter1Mode, parameter2Mode, parameter3Mode)
			instructionJump = 4
		elif opcode == 2:
			multiplyInstruction(cursorPosition, parameter1Mode, parameter2Mode, parameter3Mode)
			instructionJump = 4
		elif opcode == 3:
			saveInstruction(cursorPosition, parameter1Mode, input)
			instructionJump = 2
		elif opcode == 4:
			#print(retrieveInstruction(cursorPosition, parameter1Mode))
			output = retrieveInstruction(cursorPosition, parameter1Mode)
			instructionJump = 2
		elif opcode == 5:
			cursorPosition = jumpIfTrue(cursorPosition, parameter1Mode, parameter2Mode)
		elif opcode == 6:
			cursorPosition = jumpIfFalse(cursorPosition, parameter1Mode, parameter2Mode)
		elif opcode == 7:
			lessThen(cursorPosition, parameter1Mode, parameter2Mode, parameter3Mode)
			instructionJump = 4
		elif opcode == 8:
			equals(cursorPosition, parameter1Mode, parameter2Mode, parameter3Mode)
			instructionJump = 4

		
		if cursorPosition+instructionJump > len(data):
			break
		else:
			cursorPosition += instructionJump

	return output

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

def addInstruction(cursorPosition, parameter1Mode, parameter2Mode, parameter3Mode, data):
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

def multiplyInstruction(cursorPosition, parameter1Mode, parameter2Mode, parameter3Mode, data):
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

def saveInstructionLoop(cursorPosition, parameter1Mode, input, data):
	if parameter1Mode == 1:
		data[cursorPosition+1] = input
	else:
		data[data[cursorPosition+1]] = input

def retrieveInstruction(cursorPosition, parameter1Mode, data):
	if parameter1Mode == 1:
		return data[cursorPosition+1]
	else:
		return data[data[cursorPosition+1]]

def jumpIfTrue(cursorPosition, parameter1Mode, parameter2Mode, data):
	jumps = False
	#parameter 1
	if parameter1Mode == 1:
		if data[cursorPosition+1] != 0:
			jumps = True
	else:
		# print("DATA DO JUMP: ", data[data[cursorPosition+1]])
		if data[data[cursorPosition+1]] != 0:
			jumps = True
	#parameter 2
	if jumps == True:
		if parameter2Mode == 1:
			cursorPosition = data[cursorPosition+2]
		else:
			cursorPosition = data[data[cursorPosition+2]]
	else:
		if cursorPosition+3 < len(data):
			cursorPosition += 3

	# print("PULOU: ", jumps)
	return cursorPosition

def jumpIfFalse(cursorPosition, parameter1Mode, parameter2Mode, data):
	jumps = False

	#parameter 1
	if parameter1Mode == 1:
		if data[cursorPosition+1] == 0:
			jumps = True
	else:
		if data[data[cursorPosition+1]] == 0:
			jumps = True
	#parameter 2
	if jumps == True:
		if parameter2Mode == 1:
			cursorPosition = data[cursorPosition+2]
		else:
			cursorPosition = data[data[cursorPosition+2]]
	else:
		if cursorPosition+3 < len(data):
			cursorPosition += 3

	return cursorPosition

def lessThen(cursorPosition, parameter1Mode, parameter2Mode, parameter3Mode, data):
	# Parameter 1
	if parameter1Mode == 1:
		firstParameter = data[cursorPosition+1]
	else:
		firstParameter = data[data[cursorPosition+1]]

	# Parameter 2
	if parameter2Mode == 1:
		secondParameter = data[cursorPosition+2]
	else:
		secondParameter = data[data[cursorPosition+2]]

	# Parameter 3
	if firstParameter < secondParameter:
		if parameter3Mode == 1:
			data[cursorPosition+3] = 1
		else:
			data[data[cursorPosition+3]] = 1
	else:
		if parameter3Mode == 1:
			data[cursorPosition+3] = 0
		else:
			data[data[cursorPosition+3]] = 0

def equals(cursorPosition, parameter1Mode, parameter2Mode, parameter3Mode, data):
	# Parameter 1
	if parameter1Mode == 1:
		firstParameter = data[cursorPosition+1]
	else:
		firstParameter = data[data[cursorPosition+1]]

	# Parameter 2
	if parameter2Mode == 1:
		secondParameter = data[cursorPosition+2]
	else:
		secondParameter = data[data[cursorPosition+2]]

	# Parameter 3
	if firstParameter == secondParameter:
		if parameter3Mode == 1:
			data[cursorPosition+3] = 1
		else:
			data[data[cursorPosition+3]] = 1
	else:
		if parameter3Mode == 1:
			data[cursorPosition+3] = 0
		else:
			data[data[cursorPosition+3]] = 0

def calculateThrusterSignal(phaseSettingSequence):
	# Amp A
	phaseSettingA = phaseSettingSequence[0]
	inputA = 0
	outputA = None
	outputA = opcodeComputer([phaseSettingA, inputA], outputA)
	
	# Amp B
	phaseSettingB = phaseSettingSequence[1]
	inputB = outputA
	outputB = None
	outputB = opcodeComputer([phaseSettingB, inputB], outputB)
	
	# Amp C
	phaseSettingC = phaseSettingSequence[2]
	inputC = outputB
	outputC = None
	outputC = opcodeComputer([phaseSettingC, inputC], outputC)
	
	# Amp D
	phaseSettingD = phaseSettingSequence[3]
	inputD = outputC
	outputD = None
	outputD = opcodeComputer([phaseSettingD, inputD], outputD)
	
	# Amp E
	phaseSettingE = phaseSettingSequence[4]
	inputE = outputD
	outputE = None
	outputE = opcodeComputer([phaseSettingE, inputE], outputE)

	return outputE

def calculateMaxThrusterSignal():
	possiblePhaseSettings = [0,1,2,3,4]
	maxThrusterSignal = 0
	phasePermutations = list(itertools.permutations(possiblePhaseSettings))
	
	for permutation in phasePermutations:
		tempSignal = calculateThrusterSignal(permutation)
		if tempSignal > maxThrusterSignal:
			maxThrusterSignal = tempSignal
	

	return maxThrusterSignal

def calculateThrusterSignalLoop(phaseSettingSequence):
	inputData = open('input.txt', 'r').read().split(',')
	inputData = list(map(int, inputData))

	ampA = amplifier(phaseSettingSequence[0], inputData[:])
	ampB = amplifier(phaseSettingSequence[1], inputData[:])
	ampC = amplifier(phaseSettingSequence[2], inputData[:])
	ampD = amplifier(phaseSettingSequence[3], inputData[:])
	ampE = amplifier(phaseSettingSequence[4], inputData[:])
	

	outputSignal = 0

	while ampE.halted != True:
		outputSignal = ampA.opcodeComputerAmp(outputSignal)
		outputSignal = ampB.opcodeComputerAmp(outputSignal)
		outputSignal = ampC.opcodeComputerAmp(outputSignal)
		outputSignal = ampD.opcodeComputerAmp(outputSignal)
		outputSignal = ampE.opcodeComputerAmp(outputSignal)

	return outputSignal

def calculateMaxThrusterSignalLoop():
	possiblePhaseSettings = [5,6,7,8,9]
	maxThrusterSignal = 0
	phasePermutations = list(itertools.permutations(possiblePhaseSettings))
	for permutation in phasePermutations:
		tempSignal = calculateThrusterSignalLoop(permutation)
		if tempSignal > maxThrusterSignal:
			maxThrusterSignal = tempSignal
	

	return maxThrusterSignal


# main program part 1
#print(calculateMaxThrusterSignal())

# main program part 2
print(calculateMaxThrusterSignalLoop())


