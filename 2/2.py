input = [line.rstrip('\n') for line in open("input")]

passwords = []
for line in input:
	password = line.split(" ")
	occurance = password[0].split("-")
	passwords.append([int(occurance[0])-1,int(occurance[1])-1,password[1][0],password[2]])

valid = 0
for password in passwords:
	if (password[3][password[0]] == password[2] and password[3][password[1]] != password[2] or
		password[3][password[0]] != password[2] and password[3][password[1]] == password[2]):
			valid +=1

print(valid)

