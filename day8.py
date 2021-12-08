import pprint

inputs=''
with open('day8_inputs.txt', 'r') as inFileObj:
    inputs=[ln.split('|') for ln in inFileObj.readlines()]

inputs = [[itm[0].split(), itm[1].split()]for itm in inputs]

digitDict = {i:0 for i in range(10)}

for itm in inputs:
    for aNum in itm[1]:
        if len(aNum) == 6:
           digitDict[9] += 1
        if len(aNum) == 7:
           digitDict[8] += 1
        if len(aNum) == 3:
           digitDict[7] += 1
        if len(aNum) == 6:
           digitDict[6] += 1
        if len(aNum) == 5:
           digitDict[5] += 1
        if len(aNum) == 4:
           digitDict[4] += 1
        if len(aNum) == 5:
           digitDict[3] += 1
        if len(aNum) == 5:
           digitDict[2] += 1
        if len(aNum) == 2:
           digitDict[1] += 1
        if len(aNum) == 6:
           digitDict[0] += 1

print("Ans -- part 1 -- :", digitDict[1]+digitDict[4]+digitDict[7]+digitDict[8])

def makeNum(aNum):
    aNum = list(set(aNum))
    aNum.sort()
    aNum=''.join(aNum)
    return aNum

numList=[]
for itm in inputs:

    itm[0] =[makeNum(aNum)  for aNum in itm[0]]
    itm[1] =[makeNum(aNum)  for aNum in itm[1]]

    #find alpabets for line
    digitDict = {i:'' for i in range(8)}
    for aNum in itm[0]:

        if len(aNum) == 2:
            digitDict[1] = makeNum(aNum)
        if len(aNum) == 4:
           digitDict[4] = makeNum(aNum)
        if len(aNum) == 7:
           digitDict[8] = makeNum(aNum)
        if len(aNum) == 3:
           digitDict[7] = makeNum(aNum)

    #make 3
    for aNum in itm[0]:
        if len(aNum) == 5:
            if digitDict[1][0] in aNum and digitDict[1][1] in aNum:
                digitDict[3] = makeNum(aNum)
        
    #make 5
    bottomLeft=''.join([ltr for ltr in digitDict[8] if not ltr in digitDict[3]+digitDict[4] ])
    for aNum in itm[0]:
        if len(aNum) == 5:
            if not bottomLeft in aNum and aNum != digitDict[3] :
                digitDict[5] = makeNum(aNum)

    #make 2
    for aNum in itm[0]:
        if len(aNum) == 5 and not (aNum == digitDict[5] or aNum == digitDict[3]):
            digitDict[2] = makeNum(aNum)

    #make 6
    for aNum in itm[0]:
        if len(aNum) == 6:
            isTopRight = ''.join([ltr for ltr in digitDict[8] if not ltr in set(aNum)])
            if isTopRight in digitDict[1]:
                digitDict[6] = makeNum(aNum)
    #make 9  
    for aNum in itm[0]:
        if len(aNum) == 6:
            if not bottomLeft in aNum:
                digitDict[9] = makeNum(aNum)
    #make 0
    for aNum in itm[0]:
        if len(aNum) == 6 and not (aNum == digitDict[6] or aNum == digitDict[9]):
            digitDict[0] = makeNum(aNum)

    letterDigitDict = {itm[1]:itm[0] for itm in digitDict.items()}
   
    lineNum = []
    for alNum in itm[1]:
        keyNum = makeNum(alNum)
        lineNum.append(str(letterDigitDict[keyNum]))
    lineNum = ''.join(lineNum)
    numList.append(int(lineNum))

print("Ans -- part 2 -- :",  sum(numList) )
