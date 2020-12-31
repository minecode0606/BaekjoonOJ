score1 = int(input("1번 학생의 점수를 입력하시오> "))
score2 = int(input("2번 학생의 점수를 입력하시오> "))
score3 = int(input("3번 학생의 점수를 입력하시오> "))
score4 = int(input("4번 학생의 점수를 입력하시오> "))
score5 = int(input("5번 학생의 점수를 입력하시오> "))

total = 0
total += score1
total += score2
total += score3
total += score4
total += score5

print(f"합계는 {total} 입니다.")
print(f"평균은 {total / 5} 입니다")