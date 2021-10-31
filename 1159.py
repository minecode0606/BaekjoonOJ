import sys

N = int(sys.stdin.readline())

memo_dict = {}
outputstring = []
for _ in range(N):
    inputst = str(sys.stdin.readline())
    try:
        memo_dict[f"{inputst[0]}"] += 1
    except:
        memo_dict[f"{inputst[0]}"] = 1

for index_str in memo_dict:
    if memo_dict[index_str] >= 5:
        outputstring.append(index_str)

outputstring.sort()
if len(outputstring) == 0:
    print("PREDAJA")
else:
    for element in outputstring:
        print(element, end="")