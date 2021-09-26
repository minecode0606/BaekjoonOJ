T = int(input(""))

for _ in range(T):
    R, S = input("").split()
    R = int(R)
    for string in S:
        print(string * R, end="")
    print()

