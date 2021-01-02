# https://www.acmicpc.net/problem/2439

input01 = int(input(""))

for i in range(1, input01 + 1):
    print(" " * (input01 - i) + "*" * i)