import sys
input01 = int(input()) # 테스트 케이스 입력


for _ in range(input01): # 반복문 돌리기
    inputList1 = list(map(int, list(sys.stdin.readline().split())))
    final = inputList1[0] ** inputList1[1]
    devide = final % 10
    for i in range(1, 11):
        if devide == i:
            print(i)