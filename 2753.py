def count(input):
    if (input % 4 == 0 and input % 100 != 0) or input % 400 == 0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input01 = int(input(""))
    print(count(input01))