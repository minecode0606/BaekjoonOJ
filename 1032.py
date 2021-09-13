import sys

num = int(sys.stdin.readline().rstrip())

str_lst = []
cnt_lst = []

for i in range(num):
    string = sys.stdin.readline().rstrip()
    if num == 1:
        print(string)
        sys.exit()
    str_lst.append(string)

str_len = len(str_lst[0])
for i in range(str_len):
    cnt = 0
    for j in range(num-1):
        if str_lst[0][i] == str_lst[j+1][i]:
           cnt += 1
           if cnt == num-1:
               cnt_lst.append(str_lst[0][i])
        else:
            cnt_lst.append("?")
            break

result = ''.join(cnt_lst)
print(result)
# [출처] [백준/BOJ] 1032번 명령 프롬프트|작성자 ksil # sys 사용법 참고

