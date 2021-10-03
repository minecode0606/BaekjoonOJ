import sys
def gcd(m,n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)

inputls = list(map(int, list(sys.stdin.readline().split())))
print(gcd(int("1" * inputls[0]), int("1" * inputls[1])))