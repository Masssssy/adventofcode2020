import math
input = [line.rstrip('\n') for line in open("input")]

seatIds = []

for line in input:
	lowRow = 0
	highRow = 127
	while(line[0] == "F" or line[0] == "B"):
		mid=math.ceil((highRow+lowRow)/2)
		if(line[0] == "F"):
			highRow = mid - 1
		elif(line[0] == "B"):
			lowRow = mid 

		line = line[1:]
	row = lowRow

	lowCol = 0
	highCol = 7
	while(line[0] == "L" or line[0] == "R"):
		mid=math.ceil((highCol+lowCol)/2)
		if(line[0] == "L"):
			highCol = mid - 1 
		elif(line[0] == "R"):
			lowCol = mid +1
		if(len(line) > 1):
			line = line[1:]
		else:
			break #Done with this pass
	col = highCol

	seatIds.append(int(row*8+col))

seatIds.sort()

print("Part 1, highest id is " + str(seatIds[-1]))

currentSeat = seatIds[0]
for seat in seatIds[1:]:
	if not (seat-1 == currentSeat):
		break
	currentSeat = seat

print("Part2, my seat: " + str(seat-1))