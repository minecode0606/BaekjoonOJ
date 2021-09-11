import sys

inputls = list(map(int, list(sys.stdin.readline().split())))


A,B,C = inputls[0], inputls[1], inputls[2]

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)