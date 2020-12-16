numbers = [0,1,5,10,3,12,19]
lastVisitedAt = {}

for number in numbers[:-1]:
	lastVisitedAt[number] = numbers.index(number)+1

lastElement = numbers[-1]
for gameRound in range(len(numbers), 30000000):

	if lastElement in lastVisitedAt:
		toSpeak = gameRound - lastVisitedAt[lastElement]
	else:
		toSpeak = 0

	lastVisitedAt[lastElement] = gameRound
	lastElement  = toSpeak

	if(gameRound == 30000000-1):
		print(toSpeak)


