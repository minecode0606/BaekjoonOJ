import sys

N = int(input(""))

interls = list(map(int, list(sys.stdin.readline().split())))

M = max(interls)

remakels = []

for i in interls:
    remakels.append(i / M * 100)
total = 0
for j in remakels:
    total += j

print(total / N)