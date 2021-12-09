import pprint
import time
inputs = []
with open('day9_input.txt', 'r') as fileObj:
    inputs=fileObj.readlines()
for line in range(len(inputs)):
    inputs[line].replace('\n','')
    ln=[]
    for itm in inputs[line]:
        ln.append(int(itm)) if itm.isdigit() else ''
    inputs[line]=ln

# part 1
topEdge=0
leftEdge=0
rightEdge=len(inputs[0])
bottomEdge=len(inputs)

sumNum=[]
idxList = []
for line in range(len(inputs)):
    for idx in range(len(inputs[line])):
        compareItems=[]
        if idx+1<rightEdge:
            compareItems.append(inputs[line][idx+1])
        if idx-1>=leftEdge:
            compareItems.append(inputs[line][idx-1])
        if line+1<bottomEdge:
            compareItems.append(inputs[line+1][idx])
        if line-1>=topEdge:
            compareItems.append(inputs[line-1][idx])
        if not False in [inputs[line][idx] < cItm for cItm in compareItems]:
            sumNum.append(inputs[line][idx]+1) # risk =  height + 1
            idxList.append((line, idx)) # used for part 2
print("Ans -- part 1 -- risk :", sum(sumNum))

def untilLimit(line, idx, avoid='', visited=None):
    topEdge=0
    leftEdge=0
    rightEdge=len(inputs[0])
    bottomEdge=len(inputs)
    
    retList=[]

    if visited==None:
        visited=set([]) # using a list fills up memory and hangs up the system :'( :D
        
    if line<0 or idx<0 or (line, idx) in visited or inputs[line][idx] == 9:
        return retList,visited

    visited.add((line,idx))
    
    if inputs[line][idx]<9:
        retList.append(inputs[line][idx] )

    if (not 'right' in avoid)  and idx+1<rightEdge and inputs[line][idx+1] <9:
        extList, visitedList =untilLimit(line, idx+1, avoid+'left', visited=visited) 
        retList.extend(extList)
        visited.union(visitedList)
    if (not 'left' in avoid) and idx-1>=leftEdge  and inputs[line][idx-1]<9:
        extList, visitedList =untilLimit(line, idx-1, avoid+'right', visited=visited)
        retList.extend(extList)
        visited.union(visitedList)
    if (not 'bottom' in avoid) and line+1<bottomEdge and inputs[line+1][idx] <9:
        extList, visitedList =untilLimit(line+1, idx, avoid+'top', visited=visited)
        retList.extend(extList)
        visited.union(visitedList)
    if (not 'top' in avoid) and line-1>=topEdge and inputs[line-1][idx] <9:
        # goes on infinite recursion - have to avoid completed segments
        #retList.append(inputs[line-1][idx]) 
        extList, visitedList =untilLimit(line-1, idx, avoid+'bottom', visited=visited)
        retList.extend(extList)
        visited.union(visitedList)
    return retList, visited

basinLenList=[]
for line, idx in idxList:
    basinNums=[]
    basinNums, _ = untilLimit(line, idx, '')
    basinLenList.append(len(basinNums))
basinLenList.sort()
print("Ans -- part 2 --  biggest 3 basins {} * {} * {}:".format( basinLenList[-1],basinLenList[-2],basinLenList[-3]), basinLenList[-1]*basinLenList[-2]*basinLenList[-3])
