def cal(x1,y1,r1,x2,y2,r2):
    d = ((x2-x1)**2+(y2-y1)**2)**0.5 #원의 중심들의 거리를 d로 놓는다
    radius = r1+r2
    ra = abs(r2-r1)
    if d == 0:  # 만약 거리가 0이라면
        if r1 == r2:  # 반지름이 같으면 무한대
            return -1
        else:  # 반지름이 다르면 큰 원 안에 작은 원이 들어가 있는 경우
            return 0
    else:
        if d == radius or d == ra:  # 큰 원 안에 작은원이 한 점만 공유하면서 붙어있는 경우와 두 원이 한 점을 공유하며 붙어있는 경우
            return 1
        elif d < radius and d > ra:  # 2점을 공유하고 있는 경우
            return 2
        else:  # 두 원이 떨어져 있는 경우
            return 0

if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        x1,y1,r1,x2,y2,r2=map(int, input().split())
        print(cal( x1,y1,r1,x2,y2,r2))