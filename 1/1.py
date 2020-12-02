
input = [line.rstrip('\n') for line in open("input")]


for num in input:
	for add in input:
		for addtwo in input:
			if((int(num) + int(add) + int(addtwo)) == 2020):
				print(int(num)*int(add)*int(addtwo))
				exit()