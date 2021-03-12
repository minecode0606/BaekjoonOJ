import sys
def add(input_list):
    A, B = input_list[0], input_list[1]
    return A + B


if __name__ == '__main__':
    while True:
        input01 = list(map(int, list(sys.stdin.readline().split())))
        count = add(input01)
        print(count)