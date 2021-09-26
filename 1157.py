# input
word = input().upper()
alphabet_dict = {}
for i in range(len(word)):
    if word[i] not in alphabet_dict:
        alphabet_dict[word[i]] = 1
    else:
        alphabet_dict[word[i]] = alphabet_dict[word[i]] + 1

most_alphabet = ['?', 0]
for key, value in alphabet_dict.items():
    if most_alphabet[1] < value:
        most_alphabet[0] = key
        most_alphabet[1] = value
    elif most_alphabet[1] == value:
        most_alphabet[0] = '?'
    else:
        continue
print(most_alphabet[0])