import math
N = input("")
ls = [0] * 10

for element in N:
    element = int(element)
    if element == 6 or element == 9:
        ls[6] += 1
    else:
        ls[element] += 1

ls[6] = math.ceil(ls[6] / 2)
print(max(ls))