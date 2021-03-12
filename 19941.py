def make_list(s):
    '''이 함수는 문자열 s를 단어기준으로 자른후 리스트로 변환시켜주는 함수입니다.'''
    li = []
    for i in s:
        li.append(i)
    return li

if __name__ == '__main__':
    # 시스템 모듈을 임포트합니다
    import sys
    # 식탁의 길이 N과 햄버거를 선택할 수 있는 거리K를 입력받습니다
    inputli = list(map(int, list(sys.stdin.readline().split())))
    length = inputli[0]
    distance = inputli[1]

    # 사람과 햄버거의 위치가 문자 P(사람)와 H(햄버거)를 입력받을 뒤 리스트 자료형으로 변환합니다
    orignal_position = make_list(input(""))

    # 먹을수 있는 햄버거의 갯수를 output에 저장합니다.
    output = 0
    # 사람의 명수를 구합니다.
    p_li = []
    for array_p in orignal_position:
        if array_p == "P":
            p_li.append(array_p)
    p_len = len(p_li)
    outputlist = []
    outputcount = 0

    # 반복문을 돌립니다.
    for index_len_p in range(p_len):
        # 사람의 위치의 인덱스값을 구한후 변수 count에 대입합니다.
        count = -1
        for p_index in orignal_position:
            count += 1
            if p_index == "P":
                break
        hamburger_array = []
        for hamburger_index1 in range(distance):
            try:
                hamburger_array.append(orignal_position[(count - distance) + hamburger_index1])
            except:
                pass

        hamburger_array.append(orignal_position[count])
        for hamburger_index2 in range(distance):
            try:
                hamburger_array.append(orignal_position[(count + distance) - hamburger_index2])
            except:
                pass
        count_h_index = 0

        for select_h in hamburger_array:
            count_h_index += 1
            if select_h == "H":
                pastoutput = output

                output += 1

                try:
                    if orignal_position[count - count_h_index] == "H":
                        orignal_position[count - count_h_index] = "X"
                    if orignal_position[count + count_h_index] == "H":
                        orignal_position[count + count_h_index] = "X"
                except:
                    break
        outputlist.append(output)
        finalset = set(outputlist)
        print(output)
        print(outputlist)
        finallist = list(finalset)
        print(len(finallist))
        print(hamburger_array)

        orignal_position.remove("P")


