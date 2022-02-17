import sys

x,y,w,h = map(int, sys.stdin.readline().split())

ls = [x,y,w-x,h-y]

print(min(ls))