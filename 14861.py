def count(x_input, y_input):
    if x_input > 0:
        if y_input > 0:
            return 1
        else:
            return 4
    else:
        if y_input > 0:
            return 2
        else:
            return 3


if __name__ == '__main__':
    input01 = int(input(""))
    input02 = int(input(""))
    print(count(input01, input02))