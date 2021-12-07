import sys
import pprint

inputs=""
with open("day4_input.txt", 'r') as inputsFO:
    inputs= inputsFO.readlines()
    inputs=[itm.replace('\n', '').split() for itm in inputs ]

calledNumbers =[int(num) for num in inputs[0][0].split(',')]


matDict = {}
matCounter = 0
for itm in range(1,len(inputs)):
    if inputs[itm] == []:
        matCounter += 1
        continue
    else:
        if matCounter in matDict:
            matDict[matCounter].append([int(num) for num in inputs[itm][:]])
        else:
            matDict[matCounter]=[[int(num) for num in inputs[itm][:] ]]

matDictCols={}
for key, val in matDict.items():
    matDictCols[key] = []
    for num in range(len(val[0])):
        row=[]
        for col in range(len(val)): 
            row.append(val[col][num])
        matDictCols[key].append(row)
        
print( calledNumbers )
#pprint.pprint(matDict)
#pprint.pprint(matDictCols)

print("inputs and transpose ready\n")



""" Part 1 -- the first board """
print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n\n")
masterIndexList={}
for aDict in (matDict, matDictCols):
    for key, val in aDict.items():
        indexList=[]
        for aRow in val:
            counter=[calledNumbers.index(aNum) for aNum in aRow if aNum in calledNumbers]
            counter.sort()
            indexList.append(counter[-1]) #the index of last item in calledNumbers
        key += 100 if key in masterIndexList else 0 
        masterIndexList[key] = indexList

lowestIndex = [min(val) for key, val in masterIndexList.items()]
lowestIndex = min(lowestIndex) #minum index of called numbers for a full match
for key, val in masterIndexList.items():
    if lowestIndex in val:
        print(key)
        break
if key in matDict:
    print(matDict[key])
elif key-100 in matDict:
    print(matDict[key])

unmarked=[]
for aRow in matDict[key]:
    for aNum in aRow:
        if not aNum in calledNumbers[:lowestIndex+1]:
            unmarked.append(aNum)

print(unmarked)

print(sum(unmarked))
print(calledNumbers[lowestIndex])
print("Ans Part 1: ", sum(unmarked)*calledNumbers[lowestIndex])




""" Part 2 -- the last board """
print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n\n")
masterIndexList={}
for aDict in (matDict, matDictCols):
    for key, val in aDict.items():
        indexList=[]
        for aRow in val:
            counter=[calledNumbers.index(aNum) for aNum in aRow if aNum in calledNumbers]
            counter.sort()
            indexList.append(counter[-1]) #the index of last item in calledNumbers - the index of calledNumbers to make a row or column match
        indexList.sort()
        if key in masterIndexList:
            masterIndexList[key] =masterIndexList[key]  if masterIndexList[key] < indexList[0] else indexList[0]
        else:
            masterIndexList[key] = indexList[0]


print("called numbers length :", len(calledNumbers))
highestIndex = [val for key, val in masterIndexList.items()] 
highestIndex.sort()
highestIndex = max(highestIndex) #maximum index of called numbers (among the minimums) for a full match 
print("highest index: ", highestIndex)

matAndCall=[]
for key, val in masterIndexList.items():
    if highestIndex == val:
        print("A key is found: ", key)
        matAndCall.append(key )

print(matAndCall)
matAndCall.sort()
print(matAndCall)

key = max(matAndCall)
key -= 100 if key > 100 else 0
print("The last matrix: ", key)
if key in matDict:
    print(matDict[key])
elif key-100 in matDict:
    print(matDict[key])

unmarked=[]
for aRow in matDict[key]:
    for aNum in aRow:
        if not aNum in calledNumbers[:highestIndex+1]:
            unmarked.append(aNum)

print(unmarked)

print(sum(unmarked))
print(calledNumbers[highestIndex])
print("Ans Part 2: ", sum(unmarked)*calledNumbers[highestIndex])

