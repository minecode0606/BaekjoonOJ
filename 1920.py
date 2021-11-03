import sys

given = int(sys.stdin.readline())

array_A = list(map(int, sys.stdin.readline().split()))

given2 = int(sys.stdin.readline())

array_B = list(map(int, sys.stdin.readline().split()))

for element in array_B:
    if element in array_A:
        print("1")
    else:
        print("0")