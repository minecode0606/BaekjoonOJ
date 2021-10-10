"""
--- 전략 ---
일단 단어를 길이별로 정리하는 알고리즘 만들기
"""

class SortWord:
    @classmethod
    def sort_lenght_word(cls, ls : list) -> list:
        inputls = [[None]] * 50
        for element in ls:
            inputls[len(element)] += element
        print(inputls)

if __name__ == '__main__':
    N = int(input(""))
    inputls = []
    for _ in range(N):
        inputls.append(input(""))
    sw = SortWord()
    print(sw.sort_lenght_word(inputls))