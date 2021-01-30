import sys
def caculate():
    input_list = list(map(int, list(sys.stdin.readline().split())))
    A = list(map(str, list(reversed([int(i) for i in str(input_list[0])]))))
    B = list(map(str, list(reversed([int(j) for j in str(input_list[1])]))))
    output01 = A[0]
    A.pop(0)
    output02 = B[0]
    B.pop(0)
    for a in A:
        output01 += str(a)
    for b in B:
        output02 += str(b)
    if int(output01) <= int(output02):
        return output02
    else:
        return output01



if __name__ == "__main__":
    print(caculate())