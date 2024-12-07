data = open("data.txt", 'r')
size = 0
left = []
right = []
for line in data:
    size = size + 1
    spl = line.strip().split('   ')
    print(spl)
    left.append(int(spl[0]))
    right.append(int(spl[1]))
left = sorted(left)
right = sorted(right)
dif = 0
for x in range(size):
    dif = dif + abs(left[x] - right[x])
print(dif)
total = 0
for x in range(size):
    l = left[x]
    i = 0
    for y in range(size):
        if right[y] == l:
            i = i + 1
    total = total + (l*i)
print(total)