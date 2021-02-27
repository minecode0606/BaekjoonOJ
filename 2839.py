def count(weigh):
    outputcount = 0
    while True:
        if weigh % 5 == 0:
            outputcount += 1
            weigh = weigh - 5
        if weigh % 5 != 0:
            break

    while True:
        if weigh % 3 == 0:
            outputcount += 1
            weigh = weigh - 3
        if weigh % 3 != 0:
            break

    if weigh == 0:
        return outputcount
    elif weigh != 0:
        return -1

if __name__ == '__main__':
    input01 = int(input(""))
    print(count(input01))