def input_preprocessing(inputdata):
    """
    주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만드는 함수입니다.
    :param inputdata:
    :return inputdata:
    """
    if int(inputdata) < 10:
        inputdata = str(inputdata) + "0"
    return inputdata


# def add_cycling(input_string):
#     count = 0
#     update_num = str(int(input_string[0]) + int(input_string[1]))
#     cal_num = update_num
#
#     while str(update_num) == str(input_string):
#         pass


if __name__ == '__main__':
    # 정수 N을 입력받습니다.
    input_str = input_preprocessing(input(""))

    count = 0 # 사이클 수를 세는 변수입니다.
    result = input_str
    inputls = []
    while int(input_str) == int(result):
        for i in input_str:
            pass