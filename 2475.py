import sys

inputls = list(map(int, list(sys.stdin.readline().split())))

re = 0
for i in inputls:
    re += i ** 2
print(re % 10)