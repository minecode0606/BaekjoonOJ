import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

memo_dict = {}
for element in N_list:
    try:
        memo_dict[f"{element}"] += 1
    except:
        memo_dict[f"{element}"] = 1

for i in M_list:
    try:
        print(memo_dict[f"{i}"], end=" ")
    except:
        print("0", end=" ")