data = open("data.txt", 'r').read().split('\n')
equations = []
solutions = []
for line in data:  
    temp = line.strip().split(':')
    solutions.append(int(temp[0]))
    equations.append([int(x) for x in temp[1].strip().split(" ")])
total = 0

for x in range(len(solutions)):
    pos = [equations[x][0]]
    for num in equations[x][1:]:
        temp = []
        for po in pos:
            temp.append(num + po)
            temp.append(num * po)
            temp.append((po * 10 **(len(str(num))))+num)
        pos = temp
    if solutions[x] in pos:
        total += solutions[x]
print(total)