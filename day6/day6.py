from collections import defaultdict
from tqdm import tqdm
from copy import deepcopy
data = open("data.txt", 'r').read().split('\n')
by,bx = len(data[-1]),len(data[0])
puzzle = defaultdict(lambda: defaultdict(str))
for l,line in enumerate(data):
    for c,cha in enumerate(line):
        puzzle[l][c]= data[l][c]
        if data[l][c] == '^':
            y,x = l,c
            ty,tx = l,c
puzzle2 = deepcopy(puzzle)
facing  = 0
ny,nx = y-1,x
Exists = True
while Exists:
    if ny < 0 or ny >= by or nx < 0 or nx >= bx:
        total = 1
        for line in puzzle.values():
            for cha in line.values():
                if cha == "X":
                    total += 1
        Exists = False
    if puzzle[ny][nx] == '#':
        facing = (facing + 1) % 4
        if facing == 0:
            ny,nx = y-1,x
        if facing == 2:
            ny,nx = y+1,x 
        if facing == 1:
            ny,nx = y,x+1
        if facing == 3:
            ny,nx = y,x-1  
        continue
    
    puzzle[y][x] = 'X'

    y,x = ny,nx
    if facing == 0:
        ny,nx = y-1,x
    if facing == 2:
        ny,nx = y+1,x 
    if facing == 1:
        ny,nx = y,x+1
    if facing == 3:
        ny,nx = y,x-1
#======================================================#
part2 = puzzle
total = 0
for l,line in tqdm(enumerate(part2.values()),total = 130):
    for c,cha in enumerate(line.values()):
        test = deepcopy(puzzle2)
        if cha != 'X':
            continue
        test[l][c] = '#'
        facing = 0
        y,x = ty,tx
        ny,nx = y-1,x
        key = set()
        while not (ny < 0 or ny >= by or nx < 0 or nx >= bx):
            if test[ny][nx] == '#':
                facing = (facing + 1) % 4
                if facing == 0:
                    ny,nx = y-1,x
                if facing == 2:
                    ny,nx = y+1,x 
                if facing == 1:
                    ny,nx = y,x+1
                if facing == 3:
                    ny,nx = y,x-1  
                continue
            
            test[y][x] = 'X'
            if (facing,y,x) in key:
                total += 1
                break
            key.add((facing,y,x))
            y,x = ny,nx
            if facing == 0:
                ny,nx = y-1,x
            if facing == 2:
                ny,nx = y+1,x 
            if facing == 1:
                ny,nx = y,x+1
            if facing == 3:
                ny,nx = y,x-1
print(total)

