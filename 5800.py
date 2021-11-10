import sys

K = int(input(""))

for i in range(1, K + 1):
    print(f"Class {i}")
    inputls = list(map(int, sys.stdin.readline().split()))
    maximum = max(inputls)
    minimum = min(inputls)
    sort_inputls = sorted(inputls)
    pastmax = 0
    for j in range(len(sort_inputls) - 1):
        nowmax = sort_inputls[j + 1] - sort_inputls[j]
        if nowmax > pastmax:
            pastmax = nowmax

    print(f"Max {maximum}, Min {minimum}, Largest gap {pastmax}")

