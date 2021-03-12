input01 = int(input(""))
input02 = int(input(""))
input03 = int(input(""))
count00 = 0
count01 = 0
count02 = 0
count03 = 0
count04 = 0
count05 = 0
count06 = 0
count07 = 0
count08 = 0
count09 = 0

a = input01 * input02 * input03
list01 = list(map(int, list(str(a))))


for i in list01:
    if i == 0:
        count00 += 1
    if i == 1:
        count01 += 1
    if i == 2:
        count02 += 1
    if i == 3:
        count03 += 1
    if i == 4:
        count04 += 1
    if i == 5:
        count05 += 1
    if i == 6:
        count06 += 1
    if i == 7:
        count07 += 1
    if i == 8:
        count08 += 1
    if i == 9:
        count09 += 1

print(count00)
print(count01)
print(count02)
print(count03)
print(count04)
print(count05)
print(count06)
print(count07)
print(count08)
print(count09)
