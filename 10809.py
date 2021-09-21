inputstr = input("")

word_list = 'abcdefghijklmnopqrstuvwxyz'

for word in word_list:
    idx = 0
    for st in inputstr:
        if word == st:
            print(idx, end=" ")
            break
        else:
            idx += 1
    else:
        if word != 'z':
            print('-1', end=" ")
        else:
            print('-1' , end="")

