import sys

inputls = list(map(int, list(sys.stdin.readline().split())))

A,B = inputls[0], inputls[1]

print(A + B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)