import sys


def factor(number1, number2: int) -> str:
    """
    이 함수는 factor을 계산합니다.
    :param number1:
    :param number2:
    :return:
    """
    if number2 % number1 == 0:
        return "factor"
    else:
        return "neither"


def multiple(number1, number2: int) -> str:
    """
    이 함수는 multiple를 계산합니다.
    :param number1:
    :param number2:
    :return:
    """
    if number1 % number2 == 0:
        return "multiple"
    else:
        return "neither"


def multiples_and_factors(input_ls: list) -> str:
    input_ls = list(map(int, input_ls))

    if input_ls[0] < input_ls[1]:
        return factor(input_ls[0], input_ls[1])
    elif input_ls[0] > input_ls[1]:
        return multiple(input_ls[0], input_ls[1])
    else:
        return "neither"


if __name__ == '__main__':
    while True:
        inputls = list(map(int, list(sys.stdin.readline().split())))
        if int(inputls[0]) == 0 and int(inputls[1]) == 0:
            break
        else:
            print(multiples_and_factors(inputls))