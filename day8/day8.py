data = open("data.txt", 'r').read().split('\n')
frequency = set()
ans = set()
yb = len(data) - 1    #establish boundaries
xb = len(data[0]) - 1 
for line in data:  #create a list of frequncies to check
    for cha in line:
        if cha != '.':
            frequency.add(cha)
for freq in frequency:  #go through each frequency type
    xList = []  #setup x,y pairs of each frequency you find
    yList = []
    for l,line in enumerate(data):
        for c,cha in enumerate(line):
            if cha == freq:
                xList.append(c)
                yList.append(l)
    for c in range(len(xList)):  #go through your list of x,y pairs.  
        x = xList[c]
        y = yList[c]
        for compare in range(c+1,len(xList)):  #Creating all combinations of pairs of pairs
            slopeX = x - xList[compare]  #calculate slope between pairs
            slopeY = y - yList[compare]
            p1x = x
            p1y = y
            p2x = xList[compare]
            p2y = yList[compare]
            p1 = (p1x,p1y)    #create tuples of potential interference points
            p2 = (p2x,p2y)
            while p1x >= 0 and p1x <= xb and p1y >= 0 and p1y <= yb:  # if inbounds, add to solution set
                print(f'found ans at {p1}, using nodes {x},{y} and {xList[compare]},{yList[compare]} for freq {freq}')
                ans.add(p1)
                p1x += slopeX
                p1y += slopeY
                p1 = (p1x,p1y)
            while p2x >= 0 and p2x <= xb and p2y >= 0 and p2y <= yb: # if inbounds, add to solution set

                print(f'found ans at {p2}, using nodes {x},{y} and {xList[compare]},{yList[compare]} for freq {freq}')
                ans.add(p2)
                p2x -= slopeX
                p2y -= slopeY
                p2 = (p2x,p2y)
print(len(ans))