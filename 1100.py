def inputelement():
    outputlist = []
    for _ in range(8):
        inputstring = input("")
        for i in inputstring:
            outputlist.append(i)
    return outputlist

if __name__ == '__main__':
    inputlist = inputelement()
    count = 0
    for i in range(1, len(inputlist), 2):
        if inputlist[i] == "F":
            count += 1
    print(count)