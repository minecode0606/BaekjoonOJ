def d(n : int):
    for i in str(n):
        n += int(i)
    return n


if __name__ == '__main__':
    numberset = set()
    for i in range(1, 10001):
        numberset.add(d(i))
    for j in range(1, 10001):
        if j not in numberset:
            print(j)