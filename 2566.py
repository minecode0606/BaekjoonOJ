import sys

inputls = []


def maxinum(inputlist : list):
    maxinum = inputlist[0]
    x = 1
    y = 1
    max_x = None
    max_y = None
    for i in inputlist:
        if i > maxinum:
            maxinum = i
            max_x = x
            max_y = y
        x += 1
        if x > 9:
            x = 1
            y += 1

    return maxinum, max_y, max_x




for _ in range(9):
    inputelement = list(map(int, sys.stdin.readline().split()))
    for i in inputelement:
        inputls.append(i)

maxi, my, mx = maxinum(inputls)

print(maxi)
print(f"{my} {mx}")