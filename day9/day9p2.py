from copy import deepcopy

data = open("data.txt", 'r').read()

full = []
blank = False
count = 0
for cha in data:
    if not blank:
        full.append((blank,count,int(cha),False))  #(isEmpty,value,size,isSorted)
        count += 1
    else:
            full.append((blank,-1,int(cha),False))  #(isEmpty,value,size,isSorted)
    blank = not blank
print(full)
newFull = deepcopy(full)
f = 0
b = 0
while True:
    f = 0
    b = 0
    #print(newFull) 
    full = deepcopy(newFull)
    for revPTR in range(len(full)-1,-1,-1): #find the furthest data chunk
            reverser = full[revPTR]
            if not reverser[0]:  #check if this chunk is data
                chunk = reverser #create a temp variable for data in the rear
                for fwdPTR in range(len(full)): #find the closest large enough empty from the front
                    gasser = full[fwdPTR]  
                    if gasser[0] and gasser[3] - reverser[3] >= 0:
                        newEmptySize = gasser[3] - reverser[3] #create size for new empty chunk after data is moved
                        newFull = []
                        for i in range(len(full)): #create a new version of the full dataset
                            if i < fwdPTR:
                                newFull.append((full[i][0],full[i][1],full[i][2],True))
                            elif i == fwdPTR:
                                newFull.append((chunk[0],chunk[1],chunk[2],True))
                                if newEmptySize > 0:
                                    newFull.append((False,-1,newEmptySize,False))
                            elif i == len(full) - revPTR:
                                newFull.append(False,-1,chunk[3],True)
                            else:
                                newFull.append(full[i])
                        b = revPTR
                        f = fwdPTR
                        break
                break
    print('\n')
    final = ''
    for chunk in newFull:
        for x in range(chunk[3]):
            if chunk[0]:
                final += '.'
            else:
                final += str(chunk[1])
    print(final)
                                
                          
                    
        
        
