import sys


input01 = int(input())
inputlist = list(map(int, list(sys.stdin.readline().split())))

maximum = inputlist[0]
minimum = inputlist[0]
for i in range(0, input01):
    if maximum <= inputlist[i]:
        maximum = inputlist[i]
    if minimum >= inputlist[i]:
        minimum = inputlist[i]


print(minimum, maximum)
