data = open("data.txt", 'r').readlines()
regular = []
back = []
down = []
up = []
d1t = []
d2t = []
d1 = []
d2 = []
d3 = []
d4 = []
edit1t = []
edit2t = []
edit1 = []
edit2 = []
f1 = []
f2 = []
f3 = []
f4 = []
f1f = []
f2f = []
directions = []
final1 = []
final2 = []
for line in data:
    temp = line.strip()
    regular.append(temp)
    back.append(temp[::-1])

for x in range(len(regular)):
        templine = regular[x]
        for y in range(x):
            templine = '0' + templine
        for y in reversed(range(len(regular[x]) - x - 1)):
            templine += '0'
        d1t.append(templine)

for x in range(len(back)):
        templine = back[x]
        for y in range(x):
            templine = '0' + templine
        for y in reversed(range(len(back[x]) - x - 1)):
            templine += '0'
        d2t.append(templine)

for x in range(len(regular[0])):
          down.append('')
for x in range(len(regular[0])):
    for y in range(len(regular)):
          down[x] += regular[y][x]

for x in range(len(down)):
     up.append(down[x][::-1]) 
for x in range(len(d1t[0])):
          d1.append('')
          d2.append('')

for x in range(len(d1t[0])):
    for y in range(len(d1t)):
          d1[x] += d1t[y][x]

for x in range(len(d2t[0])):
    for y in range(len(d2t)):
          d2[x] += d2t[y][x]

for line in d1:
    d3.append(line[::-1])
for line in d2:
    d4.append(line[::-1])

total = 0

directions.append(regular)
directions.append(back)
directions.append(up)
directions.append(down)
directions.append(d1)
directions.append(d2)
directions.append(d3)
directions.append(d4)
for style in directions:
    count = 0
    for line in style:
        print(line)
        for x in range(len(line) - 3):
            if line[x:x+4] == "XMAS":
                count += 1
    print('')
    print(count)
    total += count
    print(total)
    print('')
print(total)


for line in d1:
    temp = line.replace("MAS","MBS")
    temp = temp.replace("SAM","SBM")
    edit1t.append(temp)
for line in d2:
    temp = line.replace("MAS","MBS")
    temp = temp.replace("SAM","SBM")
    edit2t.append(temp)
for x in range(len(edit1t[0])):
          edit1.append('')
          edit2.append('')

for x in range(len(edit1t[0])):
    for y in range(len(edit1t)):
        edit1[x] += edit1t[y][x]
        edit2[x] += edit2t[y][x]

for line in edit1:
    temp = line.replace('0','')
    f1.append(temp)
for line in edit2:
    temp = line.replace('0','')
    f2.append(temp)
for line in f2:
    print(line)
for line in f1:
    f3.append(line[::-1])
for line in f2:
    f4.append(line[::-1])
for x in range(len(f3)):
        templine = f3[x]
        for y in range(x):
            templine = '0' + templine
        for y in reversed(range(len(f3[x]) - x - 1)):
            templine += '0'
        f1f.append(templine)
for x in range(len(f2)):
        templine = f2[x]
        for y in range(x):
            templine = '0' + templine
        for y in reversed(range(len(f2[x]) - x - 1)):
            templine += '0'
        f2f.append(templine)

for x in range(len(f1f[0])):
          final1.append('')
          final2.append('')
for x in range(len(f1f[0])):
    for y in range(len(f1f)):
          final1[x] += f1f[y][x]

for x in range(len(f2f[0])):
    for y in range(len(f2f)):
          final2[x] += f2f[y][x]
count = 0
for line in final1:
    for x in range(len(line) - 2):
        if line[x:x+3] == "MBS" or line[x:x+3] == "SBM":
            count += 1
print(count)
