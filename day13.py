import sys
import pprint

with open(sys.argv[1], 'r') as fileObj:
    inputs=fileObj.readlines()
    inputs=[ln.replace('\n','') for ln in inputs]

pointers,folds=[],[]
x,y = [],[]
for ln in inputs:
    if ln != '':
        if 'fold' in ln:
            ln=ln.split('=')
            if 'y' in ln[0]:
                folds.append((0,int(ln[1])))
            elif 'x' in ln[0]:
                folds.append((int(ln[1]),0))
        else:
            ln = ln.split(',')
            pointers.append((int(ln[0]), int(ln[1])))
            x.append(int(ln[0]))
            y.append(int(ln[1]))

ptrMtx=[]
for _ in range((max(y)+1)):
    ptrMtx.append([' ']* (max(x)+1))
for ptr, ln in pointers:
    ptrMtx[ln][ptr] = '#'

foldCounter=0
xMax, yMax = len(ptrMtx[0]), len(ptrMtx)
for itm1, itm2 in folds:
    foldCounter += 1
    ptrMtx1, ptrMtx2 = [], []
    if itm1!=0: #fold along x
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Fold along X")
        xMax=itm1
        ptrMtx1 = [ln[:itm1] for ln in ptrMtx]
        ptrMtx1 = [ln[::-1] for ln in ptrMtx1] # fold left
        ptrMtx2 = [ln[itm1+1:] for ln in ptrMtx]
        
        if len(ptrMtx2[0]) > len(ptrMtx1[0]):
            ptrMtx1 = [ln.append(' ') for ln in ptrMtx1]
    elif itm2!=0: #fold along y
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Fold along Y")
        yMax=itm2
        ptrMtx1 = ptrMtx[:itm2]
        ptrMtx2 = ptrMtx[itm2+1:]
        ptrMtx2 = ptrMtx2[::-1] #fold up
        
        if len(ptrMtx1) > len(ptrMtx2):
            ptrMtx2 = [' ' * len(ptrMtx2)] + ptrMtx2[:]


    #print([len(ptrMtx1[0]), len(ptrMtx2[0])], [len(ptrMtx1), len(ptrMtx2)], (itm1, itm2), (xMax, yMax))
    ptrMtx=[]
    for ln in range(yMax):
        ptrMtx.append([' ']*xMax)
        for ptr in range(xMax):
            if  len(ptrMtx1) > ln and len(ptrMtx1[0]) > ptr and ptrMtx1[ln][ptr] == '#':
                ptrMtx[ln][ptr]='#'
            if  len(ptrMtx2) > ln and len(ptrMtx2[0]) > ptr and ptrMtx2[ln][ptr] == '#':
                ptrMtx[ln][ptr]='#'
    ptrSum=0
    for ln in range(len(ptrMtx)):
        for ptr in range(len(ptrMtx[0])):
            if ptrMtx[ln][ptr] == '#':
                ptrSum += 1
    if foldCounter == 1:
        print("Ans -- part 1 -- :", ptrSum, len(ptrMtx[0]), len(ptrMtx), (itm1, itm2) )

print('\n\n\n')
for ln in range(len(ptrMtx)):
    print(''.join(ptrMtx[ln])[::-1]) # i get a mirror image so flipping
