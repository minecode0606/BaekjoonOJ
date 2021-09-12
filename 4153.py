import sys # 피타고라스 나쁜놈
while True:
    inputls = list(map(int, list(sys.stdin.readline().split())))
    C = max(inputls)
    inputls.remove(C)
    A, B = inputls[0], inputls[1]
    if A == 0 & B==0 & C == 0:
        break
    elif A**2 + B**2 == C**2:
        print("right")

    else:
        print("wrong")