import sys

loopinput = int(input(""))
select_index_list = [4, 3, 2, 1]

for _ in range(loopinput):
    playerA_input_list = list(map(int, list(sys.stdin.readline().split())))
    playerB_input_list = list(map(int, list(sys.stdin.readline().split())))
    output = 0
    for index in select_index_list:
        compareA = 0
        compareB = 0
        if index in playerA_input_list:
            compareA += 1
        if index in playerB_input_list:
            compareB += 1
        if compareA > 0 or compareB > 0:
            if compareA > compareB:
                print("A")
            elif compareA < compareB:
                print("B")
            else:
                print("D")
            break