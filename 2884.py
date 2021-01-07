# https://www.acmicpc.net/problem/2884
import sys

input01 = sys.stdin.readline()
listinput = list(input01.split())

timehour = int(listinput[0])
timeminute = int(listinput[1])

if timeminute >= 45:
    timeminute = timeminute - 45
else:
    timeminute = 60 + timeminute - 45
    if timehour != 0:
        timehour -= 1
    else:
        timehour = 23


print(timehour, timeminute)
