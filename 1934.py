def check(a,b):
    small=min(a,b)
    for i in range(1,small+1):
        if a%i==0 and b%i==0:
            result=i

    ans=a*b//result
    print(ans)
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        A,B=map(int, input().split())
        check(A,B)