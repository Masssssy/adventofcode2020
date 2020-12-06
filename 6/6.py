input = [line.rstrip('\n') for line in open("input")]

groups = []
currentGroup = []
for line in input:
	if(line == ""):
		groups.append(currentGroup)
		currentGroup = []
	else:
		currentGroup.append(line)
currentGroup.append(line)
groups.append(currentGroup)

answerCount = 0
allYesCount = 0
for group in groups:
	answers = set("".join(group))
	answerCount += len(answers)

	for answer in answers:
		okToAdd = True
		for person in group:
			if not (answer in person):
				okToAdd = False
		if(okToAdd):
			allYesCount += 1

print("Part 1 " + str(answerCount))
print("Part 2 " + str(allYesCount))