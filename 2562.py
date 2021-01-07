# 정수들을 인풋합니다
input01 = int(input(""))
input02 = int(input(""))
input03 = int(input(""))
input04 = int(input(""))
input05 = int(input(""))
input06 = int(input(""))
input07 = int(input(""))
input08 = int(input(""))
input09 = int(input(""))

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
    count = "9"

print(maximum)
print(count)
