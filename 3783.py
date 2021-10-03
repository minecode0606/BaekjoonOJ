import math
T = int(input(""))

for _ in range(T):
    N = int(input(""))
    output = ('%.10f'% (math.trunc(N **(1 / 3)* 10000000000) / 10000000000))
    print(output)



from decimal import *
getcontext().prec = 1000

T = int(input())
for _ in range(T):
    n = Decimal(input())
    getcontext().rounding=ROUND_HALF_UP
    ans = round(n**(Decimal('1')/Decimal('3')),500)
    getcontext().rounding=ROUND_FLOOR
    print(round(ans,10))
#[출처] [BOJ] 3783번 - 세제곱근|작성자 박진한