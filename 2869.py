import sys

# 사용자로부터 A, B, V의 값을 입력받아서 저장합니다.
inputList = list(map(int, list(sys.stdin.readline().split())))
A = inputList[0]
B = inputList[1]
V = inputList[2]

#연산에 필요한 변수들을 지정합니다.
now = 0 # 달펭이의 현 위치
count = 0 # 몇일이 걸렸는지 카운트 하는 변수


while True: # 무한 반복문을 돌립니다.
    count += 1 # 일단. count변수에 1을 더해줍니다.
    now = now + A # 달펭이가 올라가는 연산을 수행합니다.
    if now >= V: # 만약 달펭이가 정상에 도달하였다면 반복문을 종료합니다.
        break
    now = now - B # 그렇지 않으면 밤이되니 달펭이가 미끄러 지는 연산을 수행합니다.


print(count) # 최종적으로 달펭이가 정상에 도달할때까지 걸리는 날을 출력합니다.
