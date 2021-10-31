output = 0
for _ in range(5):
    inputiter = int(input(""))
    if inputiter < 40:
        inputiter = 40
    output += inputiter

print(int(output / 5))