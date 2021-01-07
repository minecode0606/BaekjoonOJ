input01 = int(input(""))
count = 0

while True:
    if input01 % 3 == 0:
       count += 1
       input01 = input01 // 3
    if input01 % 3 != 0:
        break
while True:
    if input01 % 2 == 0:
       count += 1
       input01 = input01 // 2
    if input01 % 2 != 0:
        break
while True:
    if input01 != 1:
        count += 1
        input01 = input01 -1
    if input01 == 1:
        break
print(count)
