input = [line.rstrip('\n') for line in open("input")]

xPos = 0
yPos = 0

def takeStep(x,y, rowLen):
    global xPos
    global yPos
    xPos += x
    yPos += y
    xPos = xPos % rowLen
    return [x,y]

rows = len(input)
rowLen = len(input[0])

def calcTrees(slopeX, slopeY):
    global xPos
    global yPos
    xPos = 0
    yPos = 0
    
    trees = 0
    for b in range(1000000):
        takeStep(slopeX,slopeY, rowLen)
        if(yPos > rows-1):
            break
        elif(input[yPos][xPos] == "#"):
            trees += 1
    return trees

print(calcTrees(3,1))
print(calcTrees(1,1)*calcTrees(3,1)*calcTrees(5,1)*calcTrees(7,1)*calcTrees(1,2))
        
