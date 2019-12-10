data = open('input.txt', 'r').read().split(',')
data = list(map(int, data))
#doing the replacements specified 
data[1] = 12
data[2] = 2

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