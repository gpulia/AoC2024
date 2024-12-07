data = open("data.txt", 'r').read()
dontSegments = data.strip().split("don't()")
dat = dontSegments[0]
for strin in dontSegments[1:]:
    on = strin.split("do()")
    dat += "".join(on[1:])
print(dat)
data = dat
data = data.strip().split('mul(')
cleandata = []
for x in data:
    if len(x) > 0:
        new = x
        cleandata.append(new)
data = []
for x in cleandata:
    line = ''
    for s in x[0:]:
        if s != ')':
            line = line + s
        if s == ')':
            data.append(line)
            break
# print(data)
total = 0
for x in data:
    x = x.strip().split(',')
    mult = 0
    if len(x) == 2:
        if len(x[0]) > 0: 
            if len(x[1]) > 0:
                if x[0].isnumeric() and x[1].isnumeric():
                    a = int(x[0])
                    b = int(x[1])
                    mult = a*b

    total = total + mult
print(total)