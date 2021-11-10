import sys

n = int(sys.stdin.readline())

inputls = []
for _ in range(n):
    inputelement = int(sys.stdin.readline())
    inputls.append(inputelement)

inputls.sort()
for i in inputls:
    print(i)