ls = []
stick_length = int(input(""))

for _ in range(stick_length):
    stick_input = int(input(""))
    ls.append(stick_input)
ls.reverse()
# output = 0
maximum = ls[0]
outputls = []
for i in ls:
    if maximum <= i:
        outputls.append(i)
        # output += 1
    if maximum < i:
        maximum = i

    outputlsfinal = list(set(outputls))
print(len(outputlsfinal))