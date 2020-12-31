def fita(a, b):
    global output
    output = a**2 + b**2
    return output
while True:
    input01 = int(input("a 값 입력>"))
    input02 = int(input("b 값 입력>"))
    c = fita(input01, input02)
    print(f"c^2 = {c}")


