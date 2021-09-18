def inputelement():
    N = input("")
    F = int(input(""))
    output = []
    for i in N:
        output.append(i)
    return output, int(N), F


if __name__ == '__main__':
    inputls, N , F = inputelement()
    N = N - (int(inputls[len(inputls) - 2]) * 10 + int(inputls[len(inputls) - 1]))
    count = 0
    for i in range(N + 1):
        if N % F == 0:
            if count < 10:
                print(f"0{count}")
            else:
                print(count)
            break
        else:
            N += 1
            count += 1
