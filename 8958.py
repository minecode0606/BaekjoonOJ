def make_list(s):
    '''이 함수는 문자열 s를 단어기준으로 자른후 리스트로 변환시켜주는 함수입니다.'''
    li = []
    for i in s:
        li.append(i)
    return li

loopinput = int(input(""))

for _ in range(loopinput):
    ox_input = input("")
    ox_inputsplit = make_list(ox_input)
    countlist = []
    scorecount = 0
    scorelist = []
    for i in ox_inputsplit:
        if i == "X":
            break
        countlist.append(i)
    for j in countlist:
        scorecount += 1
        scorelist.append(scorecount)
        print(scorecount)
