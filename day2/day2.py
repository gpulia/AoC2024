dat = open("data.txt", 'r')
total = 0
data = []
for line in dat:
    stai = line.strip().split()
    stair = []
    for s in stai:
        stair.append((int(s)))
    data.append(stair)
print(data)
for stair in data:
    ok = True
    KNEES = (stair[0] - stair[1]) > 0
    if KNEES:
        print('down')
    if not KNEES:
        print('up')
    for x in range(len(stair)- 1):
        if KNEES:
            if stair[x] - stair[x+1] < 0 or abs(stair[x] - stair[x+1]) > 3 or stair[x] == stair[x+1]:
                ok = False
                stair.remove(stair[x])
        if not KNEES:
            if stair[x] - stair[x+1] > 0 or abs(stair[x] - stair[x+1]) > 3 or stair[x] == stair[x+1]:
                ok = False
                stair.remove(stair[x])
    if ok == True:
        print(line)
        total = total + 1
        
print(total)