import sys

_ = int(input(""))

inputls = list(map(int, sys.stdin.readline().split()))


delmap = list(set(inputls))

delmap.sort()
print(*delmap)