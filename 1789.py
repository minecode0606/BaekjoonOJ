S = int(input(""))

i = 1
interation = 0
index = 0
while True:
    i += 1
    interation += i
    if interation > S:
        print(i - 1)
        break
    elif interation == S:
        print(i)
        break

