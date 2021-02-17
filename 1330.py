import sys
inputList = list(map(int, list(sys.stdin.readline().split())))
count1 = int(inputList[0])
count2 = int(inputList[1])
if count1 < count2:
    print("<")
elif count1 > count2:
    print(">")
else:
    print("==")