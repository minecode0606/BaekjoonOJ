import sys
N = int(input(""))
pointls = []

for _ in range(N):
    inputls = list(map(int, list(sys.stdin.readline().split())))
    pointls.append(inputls)

pointls.sort()
for index in pointls:
    print(*index)