import sys

_ = input("")

inputls = list(map(int, sys.stdin.readline().split()))

inputls.sort()

print(*inputls)