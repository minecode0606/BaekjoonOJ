import sys

number = input("")

list01 = list(map(int, sys.stdin.readline().split()))

print(max(list01) * min(list01))