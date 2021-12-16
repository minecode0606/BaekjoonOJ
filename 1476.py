import sys

E , S , M = map(int, sys.stdin.readline().split())

nE , nS , nM = 1 , 1 , 1
count = 1
while not(nE == E and nS == S and nM == M):
    count += 1
    nE += 1
    nS += 1
    nM += 1
    if nE > 15:
        nE = 1
    if nS > 28:
        nS = 1
    if nM > 19:
        nM = 1

print(count)