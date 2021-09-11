N = int(input(""))

new = N
cycle = 0

while True:
    a = new // 10
    b = new % 10
    c = (a + b) % 10
    new = 10 * b + c
    cycle += 1
    if (N == new):
        break

print(cycle)
