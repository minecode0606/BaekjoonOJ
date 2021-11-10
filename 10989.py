import sys

N = int(sys.stdin.readline())

inputls = [0] * 10000

for _ in range(N):
    inputelement = int(input(""))
    inputls[inputelement - 1] += 1

for i in range(10000):
    for _ in range(inputls[i]):
        print(i + 1)