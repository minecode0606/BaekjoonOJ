import sys

ptr = 0
stringls = [""] * 10001
for _ in range(5):
    inputst = str(sys.stdin.readline())
    for onest in inputst:
        stringls[ptr] += onest
        ptr += 1
    ptr = 0

outputlist = ["", "", "", "", ""]
for string_element in stringls:
    if string_element == '\n\n\n\n\n' or string_element == "":
        break
    else:
        if string_element == ".omln":
            outputlist[0] += "o"
            outputlist[1] += "w"
            outputlist[2] += "l"
            outputlist[3] += "n"
            outputlist[4] += "."
        elif string_element == "owln.":
            outputlist[0] += "."
            outputlist[1] += "o"
            outputlist[2] += "m"
            outputlist[3] += "l"
            outputlist[4] += "n"
        else:
            outputlist[0] += "."
            outputlist[1] += "."
            outputlist[2] += "o"
            outputlist[3] += "L"
            outputlist[4] += "n"

for j in outputlist:
    print(j)