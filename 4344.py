import sys

def avg(list1) :   #def 함수이름(인수) :
    avg1 = sum(list1)/len(list1)  #평균 구하는 코드
    return avg1   #반환할 값


C = int(input(""))


for _ in range(C): # 기본 loop
    inputlist = list(map(int, list(sys.stdin.readline().split())))
    inputlist = inputlist[1:]
    count = 0
    mean = avg(inputlist)
    for i in inputlist:
        if i > mean:
            count += 1

    output = count / len(inputlist) * 100

    print("%.3f%%" % output)




