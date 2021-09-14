import sys
N = int(input(""))

inputls = list(map(int, list(sys.stdin.readline().split())))

maximum = max(inputls)
minimum = min(inputls)

print(maximum - minimum)