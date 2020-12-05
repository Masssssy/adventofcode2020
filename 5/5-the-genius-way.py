input = [line.rstrip('\n') for line in open("input")]

seatIds = []
for seat in input:
	binaryRow = int(seat.replace("F", "0").replace("B","1")[:-3],2)
	binaryCol = int(seat.replace("L", "0").replace("R","1")[-3:],2)
	seatIds.append(binaryRow*8 + binaryCol)
seatIds.sort()

currentSeat = seatIds[0]
for seat in seatIds[1:]:
	if not (seat-1 == currentSeat):
		break
	currentSeat = seat

print("Highest number is " + str(seatIds[-1]))
print("My seat is " + str(seat-1))