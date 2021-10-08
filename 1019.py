N = int(input(""))

wordlist = [0] * 10
for iter in range(1, N + 1):
    for number in str(iter):
        wordlist[int(number)] += 1

print(*wordlist)