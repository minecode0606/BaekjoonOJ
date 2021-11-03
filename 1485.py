import sys

T = int(sys.stdin.readline())


for _ in range(T):
    inputls = []
    for _ in range(4):
        inputelement = list(map(sys.stdin.readline().split()))
        inputls.append(inputelement)
    inputls.sort()