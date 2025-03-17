from copy import deepcopy

data = open("data.txt", 'r').read()
full = []
blank = False
count = 0
for cha in data:
    if not blank:
        for i in range(int(cha)):
            full.append(count)
        count += 1
    else:
        for i in range(int(cha)):
            full.append(-1)
    blank = not blank

data2 = deepcopy(full)


while -1 in data2:         
    for c,cha in enumerate(data2):
        if cha != -1:
            continue
        for bc,bcha in enumerate(data2[::-1]):
            if bcha != -1:
                swapper = bcha
                place = c
                fromPlace = len(data2) - bc -1
                break
        break
    print(f'{place=} {fromPlace=} {place - fromPlace}')
    if (place > fromPlace):
        break
    data2[place] = swapper
    data2[fromPlace] = -1
total = 0
for x,val in enumerate(data2):
    if val == -1:
        data2[x] = 0
for x,val in enumerate(data2):
    total += x * val
print(total)