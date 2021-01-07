import sys


inputlist01 = list(map(int, list(sys.stdin.readline().split())))
intN = inputlist01[0]
intX = inputlist01[1]
sequenceXlist = list(map(int, list(sys.stdin.readline().split())))
ls = []

for i in range(0, intN):
    if intX > sequenceXlist[i]:
        ls.append(sequenceXlist[i])

print(*ls)
