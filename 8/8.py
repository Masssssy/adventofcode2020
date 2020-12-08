def main():
	input = [line.rstrip('\n') for line in open("input")]

	opcode = []
	for op in input:
		op = op.split(" ")
		code = op[0]
		arg = int(op[1])
		opcode.append(op)

	global partOneDone 
	partOneDone = False
	#Part 1
	runOpcode(opcode) #true = Abort after p1 complete

	#Part 2
	jmpLocations = []
	nopLocations = []
	index = 0
	for code in opcode:
		if code[0] == "jmp":
			jmpLocations.append(index)
		if code[0] == "nop":
			nopLocations.append(index)
		index += 1

	for i in range(0,len(jmpLocations)):
		opcode[jmpLocations[i]][0] = "nop"
		success = runOpcode(opcode)
		opcode[jmpLocations[i]][0] = "jmp"

		if success:
			print("jmp at" + str(jmpLocations[i]))


	for i in range(0,len(nopLocations)):
		opcode[nopLocations[i]][0] = "jmp"
		success = runOpcode(opcode)
		opcode[jmpLocations[i]][0] = "nop"

		if success:
			print("nop at " + str(nopLocations[i]))

def runOpcode(thisOpcode):
	global partOneDone
	accumulator = 0
	visitedCodes = [False] * len(thisOpcode)
	currentOp = 0
	while True:

		if visitedCodes[currentOp] == True:
			if partOneDone == False:
				print("On repeating op code accumulator is: " + str(accumulator))
				partOneDone = True
			break

		visitedCodes[currentOp] = True	
		code = thisOpcode[currentOp][0]
		arg = int(thisOpcode[currentOp][1])
		if code == "acc":
			accumulator += arg
			currentOp += 1
		elif code == "jmp":
			currentOp += arg
		elif code == "nop":
			currentOp +=1

		if(currentOp == len(thisOpcode)):
			print("accumulator ON SUCCESS: " + str(accumulator))
			return True


if __name__ == "__main__":
	main()


