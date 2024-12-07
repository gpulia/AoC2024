from collections import defaultdict

data = open("data.txt", 'r').readlines()
key = defaultdict(list)
tests = []
part2 = False
for line in data:
    if len(line.strip()) == 0:
        part2 = True
    if not part2:
        pair = line.strip().split('|')
        key[int(pair[0])].append(int(pair[1]))
    if part2:
        if len(line.strip()) != 0:
            tests.append([int(x) for x in line.split(",")])
total = 0
for tri in tests:
    Good = True
    for x in range(len(tri)):
        base = tri[x]
        for y in range(1, len(tri) - x):
            if base in key[tri[x + y]]:
                Good = False
    if Good:
        # total += tri[(len(tri))//2]
        continue
    print(f'fixing [{tri}]')
    fix = tri
    
    while not Good:
        print(fix)
        Good = True
        for x in range(len(fix)):
            base = fix[x]
            for y in range(1, len(fix) - x):
                if base in key[fix[x + y]]:
                    fix[x], fix[x + y] = fix[x + y], fix[x]
                    Good = False
                    print(fix)
    total += fix[(len(fix))//2]
print(total)