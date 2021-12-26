K = int(input(""))

inputls = []
for _ in range(K):
    inputint = int(input(""))
    if inputint == 0:
        inputls.pop(len(inputls) - 1)
    else:
        inputls.append(inputint)

output = 0
for i in inputls:
    output += i
print(output)