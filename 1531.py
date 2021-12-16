import sys

# N , M을 입력받습니다.
N , M = map(int, sys.stdin.readline().split())

"""
사각형이 덮이는 갯수를 세기 위해 딕셔너리를 만듭니다.
load 형식
{"x좌표, y좌표" : int}
"""
position_dict = dict()

count = 0

for _ in range(N):
    x1 , y1 , x2 , y2 = map(int, sys.stdin.readline().split())
    for pos_y in range(y1 , y2 + 1):
        for pos_x in range(x1 , x2 + 1):
            try:
                position_dict[f"{pos_x}, {pos_y}"] += 1
            except:
                position_dict[f"{pos_x}, {pos_y}"] = 1

for index in position_dict:
    if position_dict[f"{index}"] > M:
        count += 1

print(count)