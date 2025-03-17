data = open("data.txt", 'r').read().split('\n')
first = True
nodes = {}
for line in data:
    if first:
        if line == '':
            first = False
            continue
        temp = line.split(':')
        print(temp)
        nodes.update({temp[0].strip():int(temp[1].strip())})
for item in nodes:
    print(f'{item=}')
