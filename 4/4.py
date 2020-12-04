input = [line.rstrip('\n') for line in open("input")]

passportIndex = 0
passports = {}

ids = []
for line in input:
    if line == "":
        passports[passportIndex] = ids
        passportIndex += 1
        ids = []
        continue
    else:
        lineItems = line.split()
        for item in lineItems:
            id = [item.split(":")[0], item.split(":")[1]]
            ids.append(id)

passports[passportIndex] = ids    

validPassportsCount = 0
validPassports = []
for passportId in passports:
    passport = (passports[passportId])
    passportKeys = [key[0] for key in passport]
    if 'byr' in passportKeys and 'iyr' in passportKeys and 'eyr' in passportKeys and 'hgt' in passportKeys and 'hcl' in passportKeys and 'ecl' in passportKeys and 'pid' in passportKeys:
        validPassportsCount += 1
        validPassports.append(passport)


okPasswords = 0
checks = [0,0,0,0,0,0,0]
for key in validPassports:
    passportOk = True
    for item in key:
        if(item[0] == "byr"):
            if(not(len(item[1]) == 4 and item[1].isdigit() and int(item[1]) >= 1920 and int(item[1]) <= 2002)):
                passportOk = False
                checks[0] += 1
        if(item[0] == "iyr"):
            if(not(len(item[1]) == 4 and item[1].isdigit() and int(item[1]) >= 2010 and int(item[1]) <= 2020)):
                passportOk = False
                checks[1] += 1
        if(item[0] == "eyr"):
            if(not(len(item[1]) == 4 and item[1].isdigit() and int(item[1]) >= 2020 and int(item[1]) <= 2030)):
                passportOk = False
                checks[2] += 1
        if(item[0] == "hgt"):
            unit = list(filter(lambda x: x.isalpha(), item[1]))
            unit = ''.join(unit)
            value = list(filter(lambda x: x.isdigit(), item[1]))
            value = int("".join(value))
            if(unit == "cm"):
                if(not(value >= 150 and value <= 193)):
                    passportOk = False
                    checks[3] += 1
            elif(unit == "in"):
                if(not(value >= 59 and value <= 76)):
                    passportOk = False
                    checks[3] += 1
            else:
                passportOk = False
                checks[3] += 1
        if(item[0] == "hcl"):
            firstChar = item[1][0]
            theRest = item[1][1:]
            if firstChar == "#":
                if(not len(theRest) == 6):
                    passportOk = False
                    checks[4] += 1
                else:
                    #check the actual content
                    for char in theRest:
                        if(not(char == "a" or char == "b" or char == "c" or char == "d" or char == "e" or char == "f" or char.isdigit())):
                            passportOk = False
                            checks[4] += 1
            else:
                passportOk = False
                checks[4] += 1
        if(item[0] == "ecl"):
            val = item[1]
            if(not(val == "amb" or val == "blu" or val == "brn" or val == "gry" or val == "grn" or val == "hzl" or val == "oth")):
                print(val)
                passportOk = False
                checks[5] += 1
        if(item[0] == "pid"):
            if(not(len(item[1]) == 9 and item[1].isdigit())):
                passportOk = False
                checks[6] += 1
    print(checks)
    if(passportOk):
        okPasswords += 1

print("Part 1 valid passports: " + str(validPassportsCount))
print("Part 2 valid passports " + str(okPasswords))