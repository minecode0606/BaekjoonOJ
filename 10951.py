while True:
    try:
        countlist = input("").split()
        count1, count2 = int(countlist[0]), int(countlist[1])
        print(count1 + count2)
    except:
        break