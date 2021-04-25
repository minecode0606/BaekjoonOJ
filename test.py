input = [2, 2, 2, 5, 5, 5, 6, 6, 6, 6, 6, 6, 9, 9, 11, 11, 11, 11, 11, 11]

max_input = max(input)
my_list = [0] * max_input
print(my_list)  # 11개가 생김
for i in input:
    my_list[i - 1] += 1  # input의 값 = my_list의 위치값, 나올때마다 +1하는
    # i-1을 하는 이유는 파이썬의 index는 0부터 시작하기 때문이다.
    # 즉 input의 1의 값은 my_list의 첫번째 index인 0번 index에서 +1을 하기위해서이다.
print(my_list)
# [0, 3, 0, 0, 3, 6, 0, 0, 2, 0, 6]
# 2-3번, 5-3번, 6-6번, 9-2번, 11-6번 나옴

# -------------경우1, 2의 다른 부분 ---------------#
print('my_list의 index를 1부터라고 했을 때, 최빈값은 %d 이며, 총 %d번 나왔다'
      % (my_list.index(max(my_list)) + 1, max(my_list)))
# list.index(인덱스번호 알고싶은값) => list에서 가장 최댓값의 index를 구하는 함수
# my_list.index(max(my_list)) 이 함수는 첫번째 최빈값만 불러옴.
# ------------------------------------------------#