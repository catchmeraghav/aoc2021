import time
from typing import Counter

inputs="3,5,3,1,4,4,5,5,2,1,4,3,5,1,3,5,3,2,4,3,5,3,1,1,2,1,4,5,3,1,4,5,4,3,3,4,3,1,1,2,2,4,1,1,4,3,4,4,2,4,3,1,5,1,2,3,2,4,4,1,1,1,3,3,5,1,4,5,5,2,5,3,3,1,1,2,3,3,3,1,4,1,5,1,5,3,3,1,5,3,4,3,1,4,1,1,1,2,1,2,3,2,2,4,3,5,5,4,5,3,1,4,4,2,4,4,5,1,5,3,3,5,5,4,4,1,3,2,3,1,2,4,5,3,3,5,4,1,1,5,2,5,1,5,5,4,1,1,1,1,5,3,3,4,4,2,2,1,5,1,1,1,4,4,2,2,2,2,2,5,5,2,4,4,4,1,2,5,4,5,2,5,4,3,1,1,5,4,5,3,2,3,4,1,4,1,1,3,5,1,2,5,1,1,1,5,1,1,4,2,3,4,1,3,3,2,3,1,1,4,4,3,2,1,2,1,4,2,5,4,2,5,3,2,3,3,4,1,3,5,5,1,3,4,5,1,1,3,1,2,1,1,1,1,5,1,1,2,1,4,5,2,1,5,4,2,2,5,5,1,5,1,2,1,5,2,4,3,2,3,1,1,1,2,3,1,4,3,1,2,3,2,1,3,3,2,1,2,5,2"
inputs =[int(aNum) for aNum in inputs.split(',')]

def daysAfter(days=0, inputs='' ):
    for aDay in range(days):
        inLength = len(inputs)
        newSpawn=[]
        for idx in range(len(inputs)):
            if inputs[idx] == 0:
                inputs[idx]=6
                newSpawn.append(8)
            else:
                inputs[idx] -= 1
        inputs.extend(newSpawn)
        outLength = len(inputs)
    if aDay%10 == 0:
        time.sleep(3)
    return len(inputs)

print("Ans -- part 1 -- Number after 80 days : ", daysAfter(days=80, inputs=inputs[:]) )

def dayNums(inputs=''):
    fishCounter = Counter(inputs)
    print(fishCounter)

    fishCounter[7],fishCounter[8]=0,0

    for _ in range(256):
        newFish = fishCounter[0]
        for i in range(8):
            fishCounter[i]=fishCounter[i+1]
        fishCounter[8] = newFish
        fishCounter[6] += newFish

    print(fishCounter)
    return sum([fishCounter[k] for k in fishCounter])

print("Ans -- part 2 -- Number after 256 days : ", dayNums(inputs=inputs[:]) )


