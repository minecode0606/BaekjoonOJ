import sys


N = int(input(""))

for _ in range(N):
    A, B = sys.stdin.readline().split(",")
    print(int(A) + int(B))

