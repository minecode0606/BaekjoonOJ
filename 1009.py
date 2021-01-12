import sys
input01 = int(input())


for _ in range(input01):
    inputList1 = list(map(int, list(sys.stdin.readline().split())))
    final = inputList1[0] ** inputList1[1]
    devide = final % 10
    for i in range(1, 11):
        if devide == i:
            print(i)
