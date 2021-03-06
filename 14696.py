import sys

loopinput = int(input(""))

comparecountA = 0
comparecountB = 0
forlooplist = [4, 3, 2, 1]
for _ in range(loopinput):
    playerA_card_input = list(map(int, list(sys.stdin.readline().split())))
    playerB_card_input = list(map(int, list(sys.stdin.readline().split())))

    for index in forlooplist:
        if index in playerA_card_input or index in playerB_card_input:
            for playerA_star in playerA_card_input:
                if playerA_star == index:
                    comparecountA += 1
            for playerB_star in playerB_card_input:
                if playerB_star == index:
                    comparecountB += 1
        if comparecountA == comparecountB:
            print("D")
        elif comparecountA > comparecountB:
            print("A")
        else:
            print("B")