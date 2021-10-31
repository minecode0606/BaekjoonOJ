# def add_all(ls:list):
#     """
#     This function adds up all the input list.
#     """
#     try:
#         output = 0
#         for i in ls:
#             output += int(i)
#         return output
#     except:
#         raise TypeError("Please input the right list")
#
#
# def insertion_sort(data_list):
#     """
#     This function is sorting the list
#     """
#     for stand in range(len(data_list)):
#         key = data_list[stand]
#         for num in range(stand, 0, -1):
#             if key < data_list[num - 1]:
#                 data_list[num - 1], data_list[num] = data_list[num], data_list[num - 1]
#             else:
#                 break
#     return data_list
#
#
# class Statistics:
#     def __init__(self, inputarray:list):
#         """
#         This function is input the input array
#         """
#         self.inputarray = inputarray
#         self.sort = insertion_sort(self.inputarray)
#
#     def mean(self):
#         """
#         This function returned the mean.
#         """
#         add = add_all(self.inputarray)
#         output = add / int(len(self.inputarray))
#         return round(output)
#
#     def median(self):
#         """
#         This function is returned median
#         """
#         length = len(self.inputarray)
#         if length % 2 == 0:
#             index = length // 2
#             output = (self.sort[index] + self.sort[index - 1]) / 2
#             return output
#         else:
#             index = length // 2
#             output = self.sort[index]
#             return output
#
#     def mode(self):
#         try:
#             input = self.sort
#             max_input = max(input)
#             my_list = [0] * max_input
#             for i in input:
#                 my_list[i - 1] += 1
#             return my_list.index(max(my_list)) + 1
#         except:
#             pass # continue
#     def array_range(self):
#         small = self.sort[0]
#         big = self.sort[len(self.sort) - 1]
#         output = big - small
#         return output
#
#
# if __name__ == '__main__':
#     inputls = []
#     inputlen = int(input(""))
#     for _ in range(inputlen):
#         inputint = int(input(""))
#         inputls.append(inputint)
#     st = Statistics(inputls)
#     print(st.mean())
#     print(st.median())
#     print(st.mode())
#     print(st.array_range())

import collections
import copy
class Calaulate:
    def arithmetic_mean(self, inputlist):
        """
        산술평균을 구하는 메소드입니다.
        :param inputlist:
        :return:
        """
        add = 0
        for element in inputlist:
            add += element
        return round(add / len(inputlist))
    def median(self, inputlist):
        """
        중앙값을 구하는 메소드입니다.
        :param inputlist:
        :return:
        """
        inputlist = copy.deepcopy(inputlist)
        inputlist.sort()
        while len(inputlist) != 1:
            inputlist.pop(0)
            inputlist.pop(len(inputlist) - 1)
        return inputlist[0]

    @classmethod
    def deletesubelenemt(cls, inputlist):
        """첫번째 인덱스중 최댓값보다 작은걸 제거하는 클래스메소드입니다."""
        superindex = inputlist[len(inputlist)-1][0]
        index = 0
        for detaillist in inputlist:
            if detaillist[0] < superindex:
                inputlist.pop(index)
        index += 1
        return inputlist

    def mode(self, numbers):
        """
        최빈값을 구하는 메소드입니다.
        :param numbers:
        :return:
        """
        numbers = copy.deepcopy(numbers) # 리스트를 깊은 복사합니다.
        numbers.sort() # 리스트를 내림차순으로 정렬합니다.
        maxdict = {}
        comparels = []
        for element in numbers:
            try:
                maxdict[f"{element}"] += 1
            except:
                maxdict[f"{element}"] = 1
        for index in maxdict:
            comparels.append([maxdict[index], int(index)])
        comparels.sort()
        comparels = self.deletesubelenemt(comparels)
        try:
            return comparels[1][1]
        except:
            return comparels[0][1]
    def interrange(self, inputlist):
        """
        최댓값과 최솟값의 차를 구하는 메소드입니다.
        :param inputlist:
        :return:
        """
        maximum = max(inputlist)
        minimum = min(inputlist)
        return maximum - minimum


if __name__ == '__main__':
    # 수를 입력받습니다.
    N = int(input(""))
    inputls = []
    for _ in range(N):
        inputelement = int(input(""))
        inputls.append(inputelement)

    # 계산기 인스턴스를 생성합니다.
    cal = Calaulate()
    # 산술평균을 구합니다.
    print(cal.arithmetic_mean(inputls))
    # 중앙값을 구합니다.
    print(cal.median(inputls))
    # 최빈값을 구합니다.
    print(cal.mode(inputls))
    # 범위를 구합니다.
    print(cal.interrange(inputls))
