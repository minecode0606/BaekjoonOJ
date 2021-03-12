def solve(a: list) -> int:
    count = 0
    for i in range(len(a)):
        count += a[i]
    return count

if __name__ == '__main__':
    print(solve([1, 2, 3, 4, 5]))