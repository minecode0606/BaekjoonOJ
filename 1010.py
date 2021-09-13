T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    min_x, max_x = min(x, y-x), max(x, y-x)
    answer = 1
    for i in range(min_x):
        answer *= (y-i)
    for i in range(min_x):
        answer /= (min_x -i)
    print(int(answer))
# [출처] [백준] 1010. 다리놓기|작성자 Daikoku - 조합공식을 몰라서 찾아보았습니다. (무지성의 죄)