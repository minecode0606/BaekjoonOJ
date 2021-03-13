import sys

inputlist = list(map(int, list(sys.stdin.readline().split())))


for _ in range(2):
    maximum = inputlist[0]
    for i in inputlist:
        if i > maximum:
            maximum = i
    inputlist.remove(maximum)

print(maximum)