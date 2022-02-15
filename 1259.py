while True:
    inputstr = input("")
    if inputstr == "0":
        break
    else:
        if inputstr == inputstr[::-1]:
            print("yes")
        else:
            print("no")