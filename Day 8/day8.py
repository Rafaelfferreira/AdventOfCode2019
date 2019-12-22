# reading the input
data = open('input.txt', 'r').read()

imageWidth = 25
imageHeight = 6
digitsPerLayer = imageWidth * imageHeight

cutStartingPoint = 0
cutEndingPoint = digitsPerLayer

# populating the layers
layers = []

while cutEndingPoint <= len(data):
	currentRow = []
	currentLayerData = data[cutStartingPoint:cutEndingPoint]

	lineStartingPoint = 0
	lineEndingPoint = imageWidth

	for i in range(0, imageHeight):
		currentLine = currentLayerData[lineStartingPoint:lineEndingPoint]
		currentRow.append(currentLine)
		lineStartingPoint += imageWidth
		lineEndingPoint += imageWidth

	layers.append(currentRow)

	cutStartingPoint += digitsPerLayer
	cutEndingPoint += digitsPerLayer

# searching for the layer with fewer 0s
layerWithFewer0s = 0
zerosInTheLayerWithFewerZeroes = float("inf")

for layer in range(0, len(layers)):
	zerosInThisLayer = 0
	for row in range(0,imageHeight):
		for line in range(0,imageWidth):
			if layers[layer][row][line] == '0':
				zerosInThisLayer += 1

	if zerosInThisLayer < zerosInTheLayerWithFewerZeroes:
		layerWithFewer0s = layer
		zerosInTheLayerWithFewerZeroes = zerosInThisLayer


# counting the number of 1s and 2s and multiplytin them
numberOf1s = 0
numberOf2s = 0

for row in layers[layerWithFewer0s]:
	for digit in row:
		if digit == '1':
			numberOf1s += 1
		elif digit == '2':
			numberOf2s += 1

print("Part 1 answer: ", numberOf1s * numberOf2s)
# part 2
decodedImage = []
for row in range(0, imageHeight):
	currentRow = []
	for line in range(0,imageWidth):
		currentLayer = 0
		currentPixel = None
		
		while True:
			currentPixel = layers[currentLayer][row][line]
			if currentPixel != '2':
				break
			else:
				currentLayer += 1

		currentRow.append(currentPixel)
	decodedImage.append(currentRow)

for row in decodedImage:
	line = ''
	for digit in row:
		if digit == '1':
			line += '#'
		else:
			line += ' '
	print(line)

# print("Part 2 answer: ", returnMessage)








