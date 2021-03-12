import sys

loop_input = int(input(""))
output = 0
for _ in range(loop_input):
    inputlist = list(map(int, list(sys.stdin.readline().split())))
    apple = inputlist[1]
    people = inputlist[0]
    output += apple % people
print(output)