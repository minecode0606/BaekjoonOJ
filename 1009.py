import sys
loopinput = int(input(""))

for _ in range(loopinput):
    inputlist = list(map(int, list(sys.stdin.readline().split())))
    dataset = inputlist[0] ** inputlist[1]
    computerindex = dataset % 10
    print(computerindex)