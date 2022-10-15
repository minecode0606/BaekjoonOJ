import sys


def check(a,b):
    small=min(a,b)
    for i in range(1,small+1):
        if a%i==0 and b%i==0:
            result=i

    ans=a*b//result
    return ans

def gcd(m,n):
    while n != 0:
       t = m%n
       (m,n) = (n,t)
    return abs(m)

if __name__ == '__main__':
    inputls = list(map(int, list(sys.stdin.readline().split())))
    print(gcd(inputls[0], inputls[1]))
    print(check(inputls[0], inputls[1]))