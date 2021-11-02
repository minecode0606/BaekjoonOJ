import sys

inputlist = list(map(int, sys.stdin.readline().split()))

maxinput = max(inputlist)
mininput = min(inputlist)
existarray = []
i = 1
index = 1
log = True
while log:
    for _ in range(1, i + 1):
        index += 1
        if len(existarray) >= maxinput:
            log = False
            break
        existarray.append(i)
    i += 1


j = 0
output = 0
for element in existarray:
    j += 1
    if j < mininput:
        continue
    else:
        output += element

print(output)