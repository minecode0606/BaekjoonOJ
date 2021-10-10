class EscapeSquare:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    @classmethod
    def make_positive(cls, number):
        if number < 0:
            return -number
        else:
            return number

    def compare_small_x_linear(self):
        return self.make_positive(0 - self.x)
    def compare_big_x_linear(self):
        return self.make_positive(self.w - self.h)
    def compare_small_y_linear(self):
        return self.make_positive(0 - self.y)
    def compare_big_y_linear(self):
        return self.make_positive(self.h - self.y)

if __name__ == '__main__':
    inputls = list(map(int, list(input("").split())))
    es = EscapeSquare(inputls[0], inputls[1], inputls[2], inputls[3])
    comparels = []
    comparels.append(es.compare_big_y_linear())
    comparels.append(es.compare_small_y_linear())
    comparels.append(es.compare_big_x_linear())
    comparels.append(es.compare_small_x_linear())
    print(min(comparels))