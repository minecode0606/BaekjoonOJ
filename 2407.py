import sys

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def comb(n,r):
    return factorial(n) // (factorial(r) * factorial(n-r))



inputls = list(map(int, list(sys.stdin.readline().split())))
print(comb(inputls[0], inputls[1]))



# print(math.comb(inputls[0],inputls[1]))