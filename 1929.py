# import sys
#
# # M과 N을 입력받습니다.
# M, N = sys.stdin.readline().split()
# M = int(M)
# N = int(N)
#
# # 변수를 정의합니다.
# prime = [None] * N # 소수를 저장하는 배열
# ptr: int = 0 # 소수배열의 인덱스
#
# # 사전작업을 거칩니다.
# prime[ptr] = 2 # 2는 소수이므로 초기값으로 지정
# ptr += 1 # 소수배열의 인덱스에 1 추가
#
# prime[ptr] = 3
# ptr += 1
# for n in range(3, N + 1, 2): # 3부터 홀수만 반복합니다.
#     i = 1
#     while prime[i] * prime[i] <= n:
#         if n % prime[i] == 0:
#             break
#         i += 1
#     else:
#         prime[ptr] = n
#         ptr += 1
#         if n >= M:
#             print(n)

################################################################

import sys
import math

# def getprime(num):
#     sqrt = num ** 1/2 + 1
#     if num == 1:
#         return False
#     for i in range(2, int(sqrt)):
#         if num % i == 0:
#             return False
#     return True
#
# # M과 N을 입력받습니다.
# M, N = sys.stdin.readline().split()
# M = int(M)
# N = int(N)
#
# for i in range(M, N + 1):
#     if getprime(i):
#         print(i)