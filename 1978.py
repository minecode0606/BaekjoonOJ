import sys

# 수를 입력받습니다.
N = int(input(""))
inputlist = list(map(int, list(sys.stdin.readline().split())))
maximum = max(inputlist)

ptr = 0 # 소수를 저장하는 인덱스
prime = []# 소수를 저장하는 배열

# 2는 소수이므로 소수 리스트에 추가
prime.append(2)
ptr += 1

# 3도 소수이므로 소수 리스트에 추가
prime.append(3)
ptr += 1

for n in range(5, maximum + 1, 2):
    for i in prime:
        if n % i == 0:
            break
    else:
        prime.append(n)

count = 0
for j in inputlist:
    if j in prime:
        count += 1

print(count)