import pprint
import time
import csv

inputs=[]
with open('day5_input.txt', 'r') as fileObj:
    lines = [line.replace('\n', '').split(' -> ') for line in fileObj.readlines()]
    for line in lines:
        inputs.append([[line[0].split(',')[0],line[0].split(',')[1]],
                       [line[1].split(',')[0],line[1].split(',')[1]]])

#pprint.pprint(inputs)
x, y = [], []
for itm in inputs:
    x.append(int(itm[0][0]))
    x.append(int(itm[1][0]))

    y.append(int(itm[0][1]))
    y.append(int(itm[1][1]))

x.sort()
y.sort()

print("the matrix limits : ", x[-1], y[-1])

pointers=[]
for yIdx in range(y[-1]+1):
    pointers.append([0]*(x[-1]+1))

for itm in inputs:
    x1, y1, x2, y2 = int(itm[0][0]), int(itm[0][1]), int(itm[1][0]), int(itm[1][1])
    if x1==x2 or y1 ==y2:

        xFactor = -1 if x1>x2 else 1
        yFactor = -1 if y1>y2 else 1

        while not (x1==x2 and y1==y2):
            pointers[y1][x1] += 1
            
            if x1 != x2:
                x1 += 1*xFactor
            if y1 != y2:
                y1 += 1*yFactor
        pointers[y1][x1] += 1
        print("completed -- ", x1, y1, x2, y2)
    else:
        print("skipping - not horizontal or vertical")
        
with open('outPointersHorizontalsAndVerticals.txt', 'w') as outFileObj:
    wr = csv.writer(outFileObj)
    wr.writerows(pointers)

intersect =0
for yAxis in pointers:
    for pointer in yAxis:
        if pointer > 1:
            intersect += 1

print("Ans -- Part 1 - Horizontal and Vertical intersections  :   ", intersect)


print('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n\n')

pointers=[]
for yIdx in range(y[-1]+1):
    pointers.append([0]*(x[-1]+1))

for itm in inputs:
    x1, y1, x2, y2 = int(itm[0][0]), int(itm[0][1]), int(itm[1][0]), int(itm[1][1])
    print(x1, y1, x2, y2)
    xFactor = -1 if x1>x2 else 1
    yFactor = -1 if y1>y2 else 1

    while not (x1==x2 and y1==y2):
        pointers[y1][x1] += 1
        
        if x1 != x2:
            x1 += 1*xFactor
        if y1 != y2:
            y1 += 1*yFactor
    pointers[y1][x1] += 1
    print("completed -- ", x1, y1, x2, y2)
        
with open('outPointersAll.txt', 'w') as outFileObj:
    wr = csv.writer(outFileObj)
    wr.writerows(pointers)

intersect =0
for yAxis in pointers:
    for pointer in yAxis:
        if pointer > 1:
            intersect += 1

print("Ans -- Part 2 - All intersections  :   ", intersect)
print('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n\n')
