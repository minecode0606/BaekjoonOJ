def make_positive(number):
    """입력값을 양수로 바꿉니다."""
    if number < 0:
        return -number
    else:
        return number


N = int(input("")) # N을 입력밭는다

solutionls = list(map(int, list(input("").split()))) # 용액을 입력받는다.











"""
acidicls = [] # 산성 용액이 담길 그릇
alkalinels = [] # 알칼리성 용액이 담길 그릇

# 일단 알칼리성 용액이랑 산성 용액이랑 분리합니다.
for solution_element in solutionls:
    if solution_element <= 0:
        alkalinels.append(solution_element)
    else:
        acidicls.append(solution_element)

# 비교를 위한 초기값 설정
minimum = make_positive(alkalinels[0] + acidicls[0])
minimum_alkaline = alkalinels[0]
minimum_acidicls = acidicls[0]
# 알칼리성 용액과 산성 용액을 더한값이 0에 가까운지 겁사한후 최댓값을 갱신합니다.
for alkaline_element in alkalinels:
    for acidic_element in acidicls:
        add_element = make_positive(alkaline_element + acidic_element)
        if add_element < minimum:
            minimum = add_element
            minimum_alkaline = alkaline_element
            minimum_acidicls = acidic_element

print(minimum_alkaline)
print(minimum_acidicls)
"""
"""
for index in range(N):
    # 기준값을 정하는 코드
    center = solutionls[index]
    
    # 기준값을 제외한 수들을 더하는 코드
    # 0에 근접하는지 구하는 코드
    # 만약 0 근접값이 최댓값을 넘긴다면 최댓값을 갱신, 해당 값을 정리
"""

