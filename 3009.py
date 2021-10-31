import sys

x_list = []
y_list = []
for _ in range(3):
    input_x, input_y = sys.stdin.readline().split()
    x_list.append(input_x)
    y_list.append(input_y)

x_list.sort()
y_list.sort()
if x_list[0] == x_list[1]:
    new_x = x_list[2]
else:
    new_x = x_list[0]

if y_list[0] == y_list[1]:
    new_y = y_list[2]
else:
    new_y = y_list[0]

print(f"{new_x} {new_y}")