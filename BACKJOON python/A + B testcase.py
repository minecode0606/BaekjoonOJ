import sys
add01 = 0
test_case = int(input(""))
for j in range(test_case):
    input01 = sys.stdin.readline()
    input02 = input01.split()
    list01 = list(input02)
    for i in list01:
        add01 += int(i)
    print(f"Case #{j + 1}: {add01}")
    add01 = 0