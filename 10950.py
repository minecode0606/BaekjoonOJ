add01 = 0
test_case = int(input(""))
for _ in range(test_case):
    input01 = input().split()
    list01 = list(input01)
    for i in list01:
        add01 += int(i)
    print(add01)
    add01 = 0
