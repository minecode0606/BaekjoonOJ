def distribute(kg):
    count = 0
    anothercount = 0
    anotherkg = kg

    while kg >= 5:
        count += 1
        kg -= 5
        if kg % 3 == 0:
            break
    while kg >= 3:
        count += 1
        kg -= 3

    while anotherkg >= 3:
        anothercount += 1
        anotherkg -= 3
        if anotherkg % 5 == 0:
            break
    while anotherkg >= 5:
        anothercount += 1
        anotherkg -= 5

    if kg == 0:
        return count
    elif anotherkg == 0:
        return anothercount
    else:
        return -1


if __name__ == '__main__':
    maininput01 = int(input(""))
    print(distribute(maininput01))
