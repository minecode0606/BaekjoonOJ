import math
import sys

inputint = list(map(int, list(sys.stdin.readline().split())))

print(math.comb(inputint[0], inputint[1]))