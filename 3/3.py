input = [line.rstrip('\n') for line in open("input")]

rows = len(input)
rowLen = len(input[0])

def calcTrees(slopeX, slopeY):
    pos = [0,0]
    
    trees = 0
    for b in range(rows):
        pos = takeStep(slopeX,slopeY, pos[0], pos[1],rowLen)
        if(pos[1] > rows-1):
            break
        elif(input[pos[1]][pos[0]] == "#"):
            trees += 1
    return trees

def takeStep(x,y, startX, startY, rowLen):
    return [(startX + x) % rowLen, startY + y]

print(calcTrees(3,1))
print(calcTrees(1,1)*calcTrees(3,1)*calcTrees(5,1)*calcTrees(7,1)*calcTrees(1,2))
        
