
def inputelement():
    "프롬포트에서 입력을 받은다음 전처리하는 함수입니다."
    inputstr = input("") + "."
    return inputstr

def search_polyomino_index(board:str) -> str:
    index = 0
    count_X = 0
    output = ""
    for board_element in board:
        if board_element == "X":
            count_X += 1
        if board_element == "." or count_X == 4:
            if count_X % 4 == 0:
                output += ("AAAA" * (count_X // 4))
                count_X = 0
            elif count_X % 2 == 0:
                output += ("BB" * (count_X // 2))
                count_X = 0
            else:
                return -1
            if board_element == ".":
                output += "."
    return output[0:len(output) - 1]


if __name__ == '__main__':
    inputboard = inputelement()
    print(search_polyomino_index(inputboard))

