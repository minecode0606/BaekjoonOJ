# 왼쪽 아래가 작각인 이등변 삼각형으로 * 출력하기

print("왼쪽 아래가 직각인 이등변 삼각형을 출력합니다")
n = int(input("짧은 변의 길이를 입력하세요>"))

for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print()
    

# 오른쪽 아래가 직각인 이등변 삼각형으로 * 출력하기

print("오른쪽 애래가 직각인 이등변 삼각형으로 출력합니다")
n = int(input("짧은 변의 길이를 입력하시오> "))

for i in range(n):
    for _ in range(n - i - 1):
       print(" ", d="")
    for _ in range(i + 1):
        print("*", end="")

    print()
##  엄마 나 밥묵고 올테니 컴터 만지지 마셈 ## 