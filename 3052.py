def remainder(input01, input02, input03, input04, input05,
              input06, input07, input08, input09, input10):

    input01 = input01 % 42
    input02 = input02 % 42
    input03 = input03 % 42
    input04 = input04 % 42
    input05 = input05 % 42
    input06 = input06 % 42
    input07 = input07 % 42
    input08 = input08 % 42
    input09 = input09 % 42
    input10 = input10 % 42

    inputarray = [input01, input02, input03, input04, input05,
              input06, input07, input08, input09, input10]
    ls = []
    for i in inputarray:
        if i not in inputarray:
            ls.append(i)

    return ls

if __name__ == '__main__':
    input01, input02, input03, input04, input05, input06, input07, input08, input09, input10 = int(input("")), int(input("")), int(input("")), int(input("")), int(input("")), int(input("")), int(input("")), int(input("")), int(input("")), int(input(""))
    print(remainder(input01, input02, input03, input04, input05, input06, input07, input08, input09, input10))