import sys

firstinput = list(map(int, sys.stdin.readline().split()))

list1 = list(map(int, sys.stdin.readline().split()))
list2 = list(map(int, sys.stdin.readline().split()))


addlist = list1 + list2
addlist.sort()
print(*addlist)