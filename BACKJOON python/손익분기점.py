import sys

input01 = sys.stdin.readline()
listinput = list(input01.split())

A = int(listinput[0])
B = int(listinput[1])
C = int(listinput[2])

def output(A, B, C):
    if (A / (C - B)) + 1 >= 0:

        output = A / (C - B)
        return int(output + 1)

    if B >= C:
        return -1

print(output(A, B, C))