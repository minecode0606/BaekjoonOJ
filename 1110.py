def input_preprocessing(inputdata):
    """
    주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만드는 함수입니다.
    :param inputdata:
    :return inputdata:
    """
    if int(inputdata) < 10:
        inputdata = str(inputdata) + "0"
    return inputdata


def add_cycling(input_string):
    count = 0
    update_num = str(int(input_string[0]) + int(input_string[1]))
    cal_num = update_num

    while str(update_num) == str(input_string):
        pass


if __name__ == '__main__':
    input_str = input_preprocessing(input(""))


