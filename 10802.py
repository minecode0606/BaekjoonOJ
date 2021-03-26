import sys

class Game:
    def __init__(self, inputlist):
        # 수를 입력받습니다
        self.startnumber = inputlist[0]
        self.endnumber = inputlist[1]

    def makeintarray(self):
        """ 최소값과 최댓값을 입력받은뒤 해당 박수에 들어가는 요소를 구합니다"""
        self.outputls = []
        for append in range(self.endnumber + 1):
            if append < self.startnumber:
                continue
            strappend = str(append)
            for i in strappend:
                if i == "3" or i == "6" or i == "9":
                    self.outputls.append(append)
                    continue

            if append % 3 != 0:
                continue
            self.outputls.append(append)
        return list(set(self.outputls))

    def count(self, list):
        length = len(list)
        return length % 20150523

if __name__ == '__main__':
    # 수를 입력받습니다
    inputlist = list(map(int, list(sys.stdin.readline().split())))
    game = Game(inputlist)
    array = game.makeintarray()
    print(array)
    print(game.count(array))


