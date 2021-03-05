loopinput = int(input(""))

inputlist = []
outputlist = []
for _ in range(loopinput):
    inputlist.append(int(input("")))

for _ in range(len(inputlist)):
    for i in inputlist:
        maximum = inputlist[0]
        if maximum < i:
            maximum = i
    outputlist.append(maximum)
    inputlist.remove(maximum)
print(outputlist)