# https://www.acmicpc.net/problem/2839

input01 = int(input(""))

output01 = input01 // 5 # 5kg 봉지
output02 = (input01 % 5) // 3 # 5kg 봉지의 나머지

output03 = (input01 // 3)

print(output01)
print(output02)
print(output03)

print("-----------out--------------")

if (output02 % 3) == 0 or output03 % 3 == 0:
    if output03 < output01 + output02:
        print(output03)
    else:
        print(output01 + output02)
if output02 % 3 >= 1 and output03 % 3 != 0:
    print("-1")