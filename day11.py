import sys
import pprint
import time

inputs=[]
with open(sys.argv[1], 'r' ) as fileObj:
    inputs=fileObj.readlines()

inputs = [ln.replace('\n','') for ln in inputs]
for ln in range(len(inputs)):
    tempLn=[]
    for itm in inputs[ln]:
        tempLn.append(int(itm))
    inputs[ln]=tempLn[:]

def iterateAround(inputs, ids):
    iterateIds=[]
    for col,row in ids:
        left,lefttop,top,righttop,right,rightbottom,bottom,leftbottom = (col,row-1),(col-1,row-1),(col-1,row),(col-1,row+1),(col,row+1),(col+1,row+1),(col+1,row),(col+1,row-1)
        iterateIds.extend([left,lefttop,top,righttop,right,rightbottom,bottom,leftbottom])

    ids=set([])
    for row,col in iterateIds:
        if row>=0 and row<len(inputs) and col>=0 and col<len(inputs[0]):
            inputs[row][col] = 0 if inputs[row][col]==0 else inputs[row][col]+1
            if inputs[row][col] >9:
                ids.add((row,col))      
    if ids:
       for row,col in ids:
           inputs[row][col] = 0
       inputs=iterateAround(inputs, list(ids))
    return inputs

def stepFlash(inputs):
    for row in range(len(inputs)):
        for col in range(len(inputs[0])):
            inputs[row][col] += 1

    ids=[]
    for row in range(len(inputs)):
        for col in range(len(inputs[0])):
            if inputs[row][col] >9:
                inputs[row][col]=0
                ids.append((row,col))
    
    inputs=iterateAround(inputs, ids)
    count=sum([ln.count(0) for ln in inputs])
    return inputs, count
    
count = 0
allFlashStep = 0
for step in range(10000):
    inputs, countNow = stepFlash(inputs)
    if step+1<=100:
        count += countNow
    if step+1 in range(10) or (step+1)%10 == 0 and step+1 <=100:
        #print(inputs)
        #print("Count : ", count)
        if step+1 == 100:
            print("Ans -- part 1 -- :",count)
    if countNow == 100:
        print("~>VVVVVVVVV<~")
        print("~>ALL FLASH<~  "+ str(step+1))
        print("~>^^^^^^^^^<~")
        print("Ans -- part 2 -- :", step+1)
        break

