def make_list(s):
    '''이 함수는 문자열 s를 단어기준으로 자른후 리스트로 변환시켜주는 함수입니다.'''
    li = []
    for i in s:
        li.append(i)
    return li

output = []
numberlength = (int(input("")))
for i in range(numberlength):
    i += 1
    li = make_list(str(i))
    for j in li:
        if j == "3" or j == "6" or j == "9":
            output.append(i)

print(len(output))