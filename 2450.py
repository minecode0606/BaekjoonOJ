import sys

# 총 도형의 모양의 갯수를 입력받습니다.
total = int(input(""))

# 1은 세모를, 정수 2는 네모를, 정수 3은 동그라미를 나타내는 리스트를 입력한다.
figurelist = list(map(int, list(sys.stdin.readline().split())))

# for 문을 돌리면서