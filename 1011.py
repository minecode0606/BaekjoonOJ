import sys # sys 모듈을 임포트합니다.

N = int(sys.stdin.readline()) # 케이스의 숫자를 입력받습니다.


for _ in range(N): # 태스트만큼 반복합니다.
    x, y = map(int, sys.stdin.readline().split()) # x , y값을 입력받습니다.
    distance = y - x # 두 위치 사이에 거리를 구합니다.
    number = 1
    while True:
        if number ** 2 <= distance < (number + 1) ** 2:
            """
            부등식으로 distance가 있는 수의 범위를 구합니다.
            ex) distance = 5
            epoch1 
            1 <= distance < 4
            epoch2
            4 <= distance(5) < 9 : True
            """
            break
        number += 1

    if number ** 2 == distance:
        print((number * 2) - 1)
    elif number ** 2 < distance <= (number ** 2) + number:
        print(number * 2)
    else:
        print((number * 2) + 1)