import sys
def inputdata():
    N = int(input(""))

    inputls = []
    for _ in range(N):
        inputXY = list(map(int, list(sys.stdin.readline().split())))
        inputls.append(inputXY)
    return inputls

if __name__ == '__main__':
    inputls = inputdata()
    reversels = []
    originls = []
    for i in inputls:
        i.reverse()
        reversels.append(i)
    reversels.sort()
    for j in reversels:
        j.reverse()
        originls.append(j)
    for k in originls:
        print(*k)
