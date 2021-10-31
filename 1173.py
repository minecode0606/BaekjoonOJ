class Work:
    def __init__(self):
        inputls = list(map(int, list(input("").split())))
        """ 필드 변수 사용도
        초기 맥박 : m
        운동하는 시간 : N
        최대 맥박 : M
        1분당 운동할경우 증가하는 맥박 : T
        1분당 쉴경우 감소하는 맥박 : R
        현재 맥박 : X
        """
        self.M, self.m, self.M, self.T, self.R = inputls[0], inputls[1], inputls[2], inputls[3], inputls[4]
    def workout(self):
        self.X = self.m
        minute = 0
        if self.m + self.T > self.M:
            return -1
        while True:
            if self.X + self.T < self.M:
                self.X += self.T
            elif self.X - self.R > self.m:
                self.X -= self.R
            # elif self.X == self.m
            #     minute += 1


if __name__ == '__main__':
    wo = Work()