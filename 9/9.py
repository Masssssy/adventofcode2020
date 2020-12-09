from itertools import combinations
input = [int(line.rstrip('\n')) for line in open("input")]


preamble = input[:25]
theRest = input[25:]

partOne = None

for num in theRest:
	numbers = combinations(preamble, 2)
	sums = []
	for comb in numbers:
	        sums.append(comb[0] + comb[1])

	if num in sums:
		#ok, update preamble and go again
		preamble.pop(0)
		preamble.append(num)
		continue
	else:
		print("Part 1: Failed at " + str(num))
		partOne = num
		break

startIndex = 0
startIndexFinal = None
endIndex = None
for startNum in input:
	theSum = 0
	for num in range(startIndex, len(input)):
		theSum += input[num]

		if(theSum == partOne):
			print("Found the sum startIndex is " + str(startIndex) + " last index is " + str(num))
			startIndexFinal = startIndex
			endIndex = num
			break
	if(endIndex != None):
		break
	startIndex += 1

elements = input[startIndexFinal:endIndex+1]
print("Part 2: " + str(max(elements) + min(elements)))






