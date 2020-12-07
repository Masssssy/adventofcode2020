input = [line.rstrip('\n') for line in open("input")]

bagDict = {}

for line in input:
    properties = line.split(" ")
    bagtype = properties[0] + " " + properties[1]
    if(properties[4] == "no"):
        #print("Contains no other bags")
        continue
    
    containedBags = properties[4:]
    containedBags = [i.replace(".", "") for i  in containedBags]
    containedBags = [i.replace(",", "") for i in  containedBags]
    containedBags = [i for i in containedBags if i != "bags"]
    containedBags = [i for i in containedBags if i != "bag"]
    
    bags = []
    for prop in containedBags:
        if containedBags == []:
            continue
        bag = containedBags[:3]
        containedBags = containedBags[3:]
        
        bag = [bag[0], bag[1]+ " " + bag[2]]
        bags.append(bag)    
    bagDict[bagtype] = bags
    
canHoldGoldCount = 0
for outerBag in bagDict:
    if(outerBag == "shiny gold"):
        continue
    canHoldGold = False
    toCheck = []
    
    for bag in bagDict[outerBag]:
        toCheck.append(bag)
        
    while toCheck != []:
        checking = toCheck.pop(0)
        if(checking[1] in bagDict):
            if(checking[1] == "shiny gold"):
                canHoldGold = True
                break
            for child in bagDict[checking[1]]:
                toCheck.append(child)
    if(canHoldGold):
        canHoldGoldCount += 1

bagCount = 0    
rootBag = bagDict["shiny gold"]
toCheck = []
for bag in rootBag:
    if bag[1] in bagDict:
        for b in range(0,int(bag[0])):
            toCheck.append(bag[1])
    else:
        bagCount += 1

while toCheck != []:
    checking = toCheck.pop(0)
    bagCount += 1
    
    if checking in bagDict:
        thisBag = bagDict[checking]
        for childBag in thisBag:
            for b in range(0, int(childBag[0])):
                toCheck.append(childBag[1])


print("Part 1: " + str(canHoldGoldCount))
print("Part 2: " + str(bagCount))