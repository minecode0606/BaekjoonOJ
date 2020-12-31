# https://www.acmicpc.net/problem/2562
input01 = int(input("첫번째 정수를 입력하시오> "))
input02 = int(input("두번째 정수를 입력하시오> "))
input03 = int(input("세번째 정수를 입력하시오> "))
input04 = int(input("네번째 정수를 입력하시오> "))
input05 = int(input("다섯번째 정수를 입력하시오> "))
input06 = int(input("여섯번째 정수를 입력하시오> "))
input07 = int(input("일곱번째 정수를 입력하시오> "))
input08 = int(input("여덟번째 정수를 입력하시오> "))
input09 = int(input("아홉번쨰 숫자를 입력하시오"))

maximum = input01
count = "1"
if maximum < input02:
    maximum = input02
    count = "2"
if maximum < input03:
    maximum = input03
    count = "3"
if maximum < input04:
    maximum = input04
    count = "4"
if maximum < input05:
    maximum = input05
    count = "5"
if maximum < input06:
    maximum = input06
    count = "6"
if maximum < input07:
    maximum = input07
    count = "7"
if maximum < input08:
    maximum = input08
    count = "8"
if maximum < input09:
    maximum = input09
    count ="9"

print(maximum)
print(count)