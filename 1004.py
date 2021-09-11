T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    planet = 0  # 거치는 행성계

    for _ in range(n):
        px, py, radius = map(int, input().split())
        start = (((x1 - px) ** 2) + ((y1 - py) ** 2)) ** 0.5  # 행성중심부터 시작점까지의 거리
        end = (((px - x2) ** 2) + ((py - y2) ** 2)) ** 0.5  # 행성중심부터 도착점까지의 거리

        if start < radius and end < radius:  # 시작점과 도착점 모두 원 안에 있을 경우
            pass
        elif start < radius:  # 시작점이 안에 있을 경우
            planet += 1
        elif end < radius:  # 도착점이 안에 있을 경우
            planet += 1

    print(planet)