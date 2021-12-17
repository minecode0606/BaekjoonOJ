inputls = list(map(int , input("").split()))

n = inputls[0]

inputls.pop(0)

while len(inputls) != 10:
    try:
        inputstr = map(int, input("").split())
        for element in inputstr:
            inputls.append(element)
    except:
        break

outputls = []
for i in inputls:
    str_e = str(i)
    stre =str_e[::-1]
    outputls.append(int(stre))

outputls.sort()

for j in outputls:
    print(j)