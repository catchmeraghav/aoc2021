import pprint

import sys
inputs=[]

with open(sys.argv[1],'r') as fileObj:
    inputs=fileObj.readlines()
    inputs=[ln.replace('\n','') for ln in inputs]

# Part 1
openChars = ['{','[','(','<']
closeChars = ['}',']',')','>']

closeVals = { '}':1197, ']':57, ')':3, '>':25137 }

totalCount=0

for ln in inputs:
    corruptCount=0
    lastOpen=[]
    for idx in range(len(ln)):
        
        if ln[idx] in openChars:
            lastOpen.append(ln[idx])

        if ln[idx] in closeChars:
            if lastOpen[-1] != openChars[closeChars.index(ln[idx])] :
                corruptCount += closeVals[ ln[idx] ]
            lastOpen.pop()

    if corruptCount:
        totalCount += corruptCount
print("Ans -- part 1 : ", totalCount)

#part 2
completeVals = { '}':3, ']':2, ')':1, '>':4 }
scoreList=[]
for ln in inputs:
    corruptCount=0
    lastOpen=[]
    for idx in range(len(ln)):
        if ln[idx] in openChars:
            lastOpen.append(ln[idx])

        if ln[idx] in closeChars:
            if lastOpen[-1] != openChars[closeChars.index(ln[idx])] :
                corruptCount += closeVals[ ln[idx] ]
            lastOpen.pop()
    lnScore=0
    if not corruptCount:
        for itm in lastOpen[::-1]:
            lnScore = lnScore*5 + completeVals[ closeChars[openChars.index(itm)]  ]
        scoreList.append(lnScore)
        
scoreList.sort()
print("Ans -- part 2 : ", scoreList[((len(scoreList)-1)/2)])
