import sys
testcase = int(sys.stdin.readline())
for _ in range(testcase):
    inputlist = list(map(int, list(sys.stdin.readline().split())))
    base, up = inputlist[0] , inputlist[1]
    if up % 4 == 0:
        up = 4
    else:
        up = up % 4
    dataset = base ** up % 10
    # computerindex = dataset % 10
    print(dataset)