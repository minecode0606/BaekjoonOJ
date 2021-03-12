def make_list(s):
    '''이 함수는 문자열 s를 단어기준으로 자른후 리스트로 변환시켜주는 함수입니다.'''
    li = []
    for i in s:
        li.append(i)
    return li

# 반복문을 돌려 입력값을 입력받아 반복문을 돌립니다
loopinput = int(input(""))
output = 0
# 인풋을 리스트로 쪼갭니다.
for _ in range(loopinput):
    ox_input = input("")
    ox_inputsplit = make_list(ox_input)
    print(ox_inputsplit)
    ox_listindex = 0
    # O의 최종 인덱스를 찿아서 연산합니다.
    for i in ox_inputsplit:
        if i == "X":
            ox_listindex = 0
            ox_inputsplit.remove("X")
            break
        ox_listindex += 1
        output += ox_listindex
    print(output)