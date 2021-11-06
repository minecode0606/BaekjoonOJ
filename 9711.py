import sys

c = int(input(""))
for k in range(1, c + 1):
    n, m = map(int, sys.stdin.readline().split())

    fib = [0,1]
    remove = -1
    for i in range(2,n + 1 ):
        fib.append(fib[0] + fib[1])
        remove += 1
        fib.pop(0)

    print(f"Case #{k}: {fib[1] % m}")